import pyautogui as pg
import os
import subprocess
import time as t

subprocess.Popen('mspaint.exe')

t.sleep(1)

location =pg.locateOnScreen('brush_on.png')
print('Bubble: ',location)

print(location.left)

# if location != None:
#     pg.moveTo(118,343)
#     pg.dragTo(891,828,button='left')

if location.left<=600 and location.top<=600:
    pg.click("bubble.png",clicks=3)
    t.sleep(1)
    pg.moveTo(118,343)
    pg.dragTo(891,828,button='left')