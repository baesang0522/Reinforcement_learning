import pywinauto as pwa
import pyautogui as pg
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
    def __init__(self):
        self.window = set_focus_on_process(process_nm=config.PROCESS_NM)
        pg.click(**config.CLICK_ON_BLUESTACKS)

    def turn_left(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["left"])

    def turn_right(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["right"])

    def drift_left_start(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["left_drift_start"])

    def drift_left_end(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["left_drift_end"])

    def drift_right_start(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["right_drift_start"])

    def drift_right_end(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["right_drift_end"])

    def kart_break(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["break"])

    def restart_game(self):
        pwa.keyboard.send_keys(config.CTL_KEY_SET["pause_game"])
        pwa.keyboard.send_keys(config.CTL_KEY_SET["restart_game"])

