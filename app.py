from flask import Flask
import os

from .alarm_clock import AlarmClock

alarm = AlarmClock(os.path.join('.', 'good-morning.mp3'))
app = Flask(__name__)

alarm.sound()

@app.route('/sound')
def sound():
    alarm.sound()
t
@app.route('/stop')
def stop():
    alarm.stop()

@app.route('/snooze')
def snooze():
    alarm.snooze()
