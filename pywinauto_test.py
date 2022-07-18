import os
import sys
import time
import pyautogui
import pywinauto as pwa


def set_focus(title_reg):
    app = pwa.application.Application()
    t = title_reg

    try:
        handle = pwa.findwindows.find_windows(title_re=t)[0]
        app.connect(handle=handle)
        print("title: " + str(t) + "handle: " + str(handle) + "set")
    except:
        print("Error occurred... No title exist on window")

    window = app.window(handle=handle)

    try:
        window.set_focus()
    except Exception as e:
        print(f"Error in set_focus: {e}")

    return window


def set_focus_bluestacks():
    t = u'BlueStack*'
    return set_focus(title_reg=t)


aa = set_focus_bluestacks()