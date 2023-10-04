from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time as t

path=r'C:\Users\ASUS\OneDrive\เดสก์ท็อป\Rpa_thing\practice2\chromedriver.exe'
service=Service(path)

driver = webdriver.Chrome(service=service)
driver.get("https://uncle-tools.com/admin/login/?next=/admin/%3Ffbclid%3DIwAR0pYaqfnqNt4PrUSzX0Q0jzVDqBcnWOzJayl-NVnAqst55tYkhh7ccFWJE")

username=driver.find_element(By.NAME,'username')
username.send_keys('uncle')
t.sleep(5)

password=driver.find_element(By.NAME,'password')
password.send_keys('Admin12345')
password.send_keys(Keys.RETURN)
t.sleep(2)

url='https://uncle-tools.com/admin/myapp/product/add/'
driver.get(url)

fruit=[['มะม่วง',20],['ทุเรียน',40],['ส้ม',25]]

for i,j in fruit:
    name=driver.find_element(By.NAME,'name')
    name.send_keys(i)
    t.sleep(5)

    price=driver.find_element(By.NAME,'price')
    price.clear()#ล้างค่าที่มีอยู่ก่อนที่จะกรอกออกไป
    price.send_keys(j)
    t.sleep(5)

    # save=driver.find_element(By.NAME,'_save')
    # save.click()
    saveadd=driver.find_element(By.NAME,'_addanother')
    saveadd.click()	
    t.sleep(5)

t.sleep(60)
driver.quit()