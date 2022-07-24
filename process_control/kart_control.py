import pywinauto as pwa
from process_control import config


def set_focus_on_process(process_nm):
    app = pwa.application.Application()

    try:
        handle = pwa.findwindows.find_windows(title_re=process_nm)[0]
        app.connect(handle=handle)
        print("title: " + str(process_nm) + "handle: " + str(handle) + "set")
        window = app.window(handle=handle)
        window.set_focus()
        return window

    except IndexError:
        print(f"No process named \"{process_nm}\". Please check again")


class KartController:
    def __init__(self, process_nm):
        self.window = set_focus_on_process(process_nm=config.PROCESS_NM)

    def control(self):
        pass


app = pwa.application.Application()
handle = pwa.findwindows.find_windows(title_re=u'BlueStack*')[0]
app.connect(handle=handle)
print("title: " + str(u'BlueStack*') + "handle: " + str(handle) + "set")
window = app.window(handle=handle)
window.set_focus()