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


@app.route("/api/tv/power")
def power():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_POWER'])
    return "Power!"


@app.route("/api/tv/volumeup")
def volumeup():
    for index in range(5):
        time.sleep(0.5)
        subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEUP'])
    #subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEUP','KEY_VOLUMEUP','KEY_VOLUMEUP','KEY_VOLUMEUP','KEY_VOLUMEUP'])
    return "volumeup!"


@app.route("/api/tv/volumedown")
def volumedown():
    for index in range(5):
        time.sleep(0.5)
        subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEDOWN'])
    #subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN','KEY_VOLUMEDOWN'])
    return "volumedown!"


@app.route("/api/tv/mute")
def mute():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_MUTE'])
    return "mute!"


@app.route("/api/tv/channelup")
def channelup():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_CHANNELUP'])
    return "channelup!"


@app.route("/api/tv/channeldown")
def channeldown():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_CHANNELDOWN'])
    return "channeldown!"


@app.route("/api/tv/input")
def input():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_INPUT'])
    return "input!"


@app.route("/api/tv/back")
def back():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_RETURN'])
    return "return!"


@app.route("/api/tv/up")
def up():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_UP'])
    return "up!"


@app.route("/api/tv/down")
def down():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_DOWN'])
    return "down!"


@app.route("/api/tv/left")
def left():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_LEFT'])
    return "left!"


@app.route("/api/tv/right")
def right():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_RIGHT'])
    return "right!"


@app.route("/api/tv/apps")
def apps():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_APPS'])
    return "apps!"


@app.route("/api/tv/ok")
def ok():
    subprocess.call(['irsend','SEND_ONCE','livingroomtv','KEY_OK'])
    return "ok!"


@app.route('/api/tv/command/<cmd>')
def command(cmd):
    strcmd = 'KEY_' + cmd.upper()
    subprocess.call(['irsend','SEND_ONCE','livingroomtv',strcmd])
    return strcmd


if __name__ == "__main__":
    app.run(host='0.0.0.0')