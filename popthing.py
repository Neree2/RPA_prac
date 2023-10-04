import webbrowser as wb
import time
import pyautogui as pg
wb.open('https://www.google.com')
time.sleep(1)
pg.write('pop cat')
time.sleep(1)
pg.press('enter')
time.sleep(1)
pg.click(304,396)
time.sleep(1)
pg.click(1053,499,clicks=10)
time.sleep(1)
pg.screenshot('popcatthing.png')
