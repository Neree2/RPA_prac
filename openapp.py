import webbrowser as wb
import time as t
import pyautogui as pg
pg.moveTo(419,1052)
t.sleep(1)
pg.click(419,1052)
t.sleep(1)
pg.write('vscode')
t.sleep(1)
pg.moveTo(411,276)
t.sleep(1)
pg.click(411,276)
t.sleep(1)
pg.screenshot('openthings.png')
