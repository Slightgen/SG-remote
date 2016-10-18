#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import commands

app = Flask(__name__)


available = ['power', 'fileviewer', 'show_desktop',
             'alt_tab', 'enter', 'F5', 'close', 'cut',
             'copy', 'paste', 'backspace', 'pageup',
             'pagedown', 'left', 'right', 'up', 'down',
             'escape', 'home', 'end', 'tab', 'startup_menu', ]

@app.route('/exe/<command>')
def exe_command(command):
    if command in available:
        print "data in available" + command
        getattr(commands, command)()
        return("executed")
    else:
        print("invalid command")
        return("invalid_command")


@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
