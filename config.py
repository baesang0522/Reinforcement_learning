import torch


class Config:
    PROCESS_NM = u'BlueStack*'
    CTL_KEY_SET = {
        "LEFT": "{LEFT}",
        "RIGHT": "{RIGHT}",
        "BREAK": "{DOWN}",
        "DRIFT": "{VK_SHIFT}",
        "START_BOOSTER": "{VK_RSHIFT}",
        "TEMP_BOOSTER": "{UP}",
        "PAUSE_GAME": "{INSERT}",
        "RESTART_GAME": "{END}"
    }


class DevConfig(Config):
    pass


class ProdConfig(Config):
    pass




