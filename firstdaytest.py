
import pyautogui
# import pyautogui as pg
#สั้นขึ้น
# easier to do in idleshell python
#window screen width and height
print(pyautogui.size())
# พิกัดตามที่เม้าเราไปวาง
print(pyautogui.position())
# เม้าจะเลื่อนไปตามพิกัดและกด
pyautogui.click(1797,1025)
#เลื่อนไปและกดตามจำนวนครั้งที่เรากำหนดใน clicks
pyautogui.click(1797,1025,clicks=3)
#move to ที่ที่เรากำหนดแต่ไม่กด
pyautogui.moveTo(1670.59)
#วิ่งไปในความเร็วเท่าไหร่มันจะคำนวนเอง
pyautogui.moveTo(1670.59,duration=10)