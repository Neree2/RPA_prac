import webbrowser as wb
import time as t
import pyautogui as pg
wb.open('https://www.google.com')
t.sleep(1)
pg.write('calculator google')
t.sleep(1)
pg.click(768,568)
t.sleep(1)
pg.click(991,570)
t.sleep(1)
pg.click(991,570)
t.sleep(1)
pg.click(887,672)
t.sleep(1)
pg.screenshot('calculatorthing.png')
