#!/usr/bin/env python
# -*- coding: utf-8 -*-


from datetime import datetime
import commands

import lirc
import sys


prev = datetime.now().microsecond
current =datetime.now().microsecond

print("import success")
print("ready")

available = ['power' ,'fileviewer' ,'show_desktop' ,\
              'alt_tab' ,'enter' ,'F5' ,'close' ,'cut' ,\
              'copy' ,'paste' ,'backspace' ,'pageup' ,\
              'pagedown' ,'left' ,'right' ,'up','down' ,\
              'escape', 'home' ,'end' ,'tab']

sockid = lirc.init("remote")

def start():
    """
    start() method start the listener for IR input from remote
    controller.
    """
    while True:
        try:
            current = datetime.now().microsecond
            code = lirc.nextcode()
            print(code[0])
            if code and code[0] in available:
                getattr(commands,code[0])()
            else:
                print("invalid command")
        except:
            continue
