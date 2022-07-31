import time
import pyautogui as pag
import mss, cv2
import numpy as np


while True:
    time.sleep(1)
    x, y = pag.position()
    position_str = 'X: ' + str(x) + ' Y: ' + str(y)
    print(position_str)

"""
left = {X: 235, Y: 873}
right = {X: 495, Y:866}
break = {X: 1417 Y: 1003}
drift = {X: 1690, Y: 886}
booster = {X: 1600, Y: 628}
temp_booster = {X: 1435, Y: 741}
pause_game = {X: 1726, Y: 67}
reset_game = {X: 969, Y: 1045}
"""


from PIL import ImageGrab
import cv2
import keyboard
import mouse
import numpy as np

def set_roi():
    global ROI_SET, x1, y1, x2, y2
    ROI_SET = False
    print("Select your ROI using mouse drag.")
    while(mouse.is_pressed() == False):
        x1, y1 = mouse.get_position()
        while(mouse.is_pressed() == True):
            x2, y2 = mouse.get_position()
            while(mouse.is_pressed() == False):
                print("Your ROI : {0}, {1}, {2}, {3}".format(x1, y1, x2, y2))
                ROI_SET = True
                return
keyboard.add_hotkey("ctrl+1", lambda: set_roi())
ROI_SET = True
x1, y1, x2, y2 = 0, 0, 1111, 1951
while True:
    if ROI_SET == True:
        image = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2))), cv2.COLOR_BGR2RGB)
        cv2.imshow("image", image)
        key = cv2.waitKey(100)
        if key == ord("q"):
            print("Quit")
            break
cv2.destroyAllWindows()


im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
im.show()