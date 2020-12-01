#!/usr/bin/env python3
import subprocess
import time
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    #return "Hello World!"
    return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route("/api/tv/")
def tv():
    return "TV!"


@app.route('/api/tv/command/<cmd>')
def command(cmd):

    cmd = cmd.split("-")
    if len(cmd) == 1:
        strcmd = 'KEY_' + cmd[0].upper()
        if 'VOLUME' in strcmd:
            execcmdmultimes(strcmd, 5)   
        else:
            subprocess.call(['irsend','SEND_ONCE','livingroomtv',strcmd])
        return strcmd
    elif not 'channelto' in cmd[0]:
        strcmd = cmd[0]
        strtimes = cmd[1]
        execincdec(strcmd, strtimes)
    elif cmd[0] == 'channelto':
        channel = cmd[1]
        execchannelto(channel)
  
    return cmd[0]


def execincdec(strcmd, strtimes):
    if strcmd == "channelincreaseby":
        strcmd = 'KEY_' + "channelup"
        execcmdmultimes(strcmd, strtimes)

    elif strcmd == "channeldecreaseby":
        strcmd = 'KEY_' + "channeldown"
        execcmdmultimes(strcmd, strtimes)
    elif strcmd == "volumeupby":
        strcmd = 'KEY_' + "volumeup"
        execcmdmultimes(strcmd, strtimes)
    elif strcmd == "volumedownby":
        strcmd = 'KEY_' + "volumedown"
        execcmdmultimes(strcmd, strtimes)              


def execcmdmultimes(strcmd, strtimes):
    for index in range(int(strtimes)):
        time.sleep(0.5)
        subprocess.call(['irsend','SEND_ONCE','livingroomtv',strcmd])        


def execchannelto(channel):
    for index in channel:
        strcmd = 'KEY_' + index
        time.sleep(0.5)
        subprocess.call(['irsend','SEND_ONCE','livingroomtv',strcmd])    


if __name__ == "__main__":
    app.run(host='0.0.0.0')