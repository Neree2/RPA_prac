from songline import Sendline

#token สำหรับบอทที่ชื่อ...ส่งเข้าน เณคนเดียว
token='sLS9CxSjA3Bb4BBVqpDCjlzw06gyIDKCODDaDOQp1JN'

m=Sendline(token)
m.sendtext('Hello World')

m.sticker(6,1,'ร้อน')

m.sendimage('https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcS4WH3Cpe1X75X4LhbHdyJo3vPEs0ufiHQhHjkqEnMjbPqViSEVI-nqF0NpeLscSR-7')

path=r'C:\Users\ASUS\OneDrive\เดสก์ท็อป\Rpa_thing\screen.png'
m.sendimage_file(path)