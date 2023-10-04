import pyautogui as pg
import os
import subprocess
import time as t

subprocess.Popen('mspaint.exe')
# subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe')#เฉพาะ program ใน system ที่ window รู้จัก

t.sleep(1)

location =pg.locateOnScreen('painty.png')
print(location)




# path=os.getcwd()#current working directory
# print(path)

# image='painty.png'
# fullpath=os.path.join(path,image)
# print(fullpath)

# folder='img'

# fullpath_folder=os.path.join(path,folder)
# fullpath_image_folder=os.path.join(fullpath_folder,image)
# print(fullpath_image_folder)