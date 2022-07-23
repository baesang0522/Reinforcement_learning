import pywinauto as pwa


class KartController:
    def __init__(self, process_nm):
        self.process_nm = process_nm

    def set_focus_on_process(self):
        app = pwa.application.Application()

        try:
            handle = pwa.findwindows.find_windows(title_re=self.process_nm)[0]
            app.connect(handle=handle)
            print("title: " + str(self.process_nm) + "handle: " + str(handle) + "set")
            window = app.window(handle=handle)
            window.set_focus()
            return window

        except IndexError:
            print(f"No process named \"{self.process_nm}\". Please check again")
