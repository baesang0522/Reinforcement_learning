import torch


class Config:
    PROCESS_NM = u'BlueStack*'
    CTL_KEY_SET = {
        "left": "{LEFT}",
        "left_drift_start": "{LEFT down} {VK_SHIFT down}",
        "left_drift_end": "{LEFT up} {VK_SHIFT up}",
        "right": "{RIGHT}",
        "right_drift_start": "{RIGHT down} {VK_SHIFT down}",
        "right_drift_end": "{RIGHT up} {VK_SHIFT down}",
        "break": "{DOWN}",
        "drift": "{VK_SHIFT}",
        "start_booster": "{VK_RSHIFT}",
        "temp_booster": "{UP}",
        "pause_game": "{INSERT}",
        "restart_game": "{END}"
    }
    CLICK_ON_BLUESTACKS = {"X": 21, "Y": 18}


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass




