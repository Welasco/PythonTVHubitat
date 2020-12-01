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
    strcmd = 'KEY_' + cmd.upper()
    if 'VOLUME' in strcmd:
        for index in range(5):
            time.sleep(0.5)
            subprocess.call(['irsend','SEND_ONCE','livingroomtv',strcmd])          
    else:
        subprocess.call(['irsend','SEND_ONCE','livingroomtv',strcmd])
    return strcmd


if __name__ == "__main__":
    app.run(host='0.0.0.0')