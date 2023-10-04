import webbrowser as wb
import time
import pyautogui as pg
wb.open('https://www.google.com')
time.sleep(2)
pg.write('jpy to thb')
time.sleep(3)
pg.press('enter')
#ทำให้ช้าขึ้นท่วงเวลา sleep
time.sleep(2)
pg.screenshot('jpy to thb.png')
