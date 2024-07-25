# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")
# print('wait for login time')
# time.sleep(30)
#
# Contact = driver.find_element(By.TAG_NAME, "Nene")
# Contact.click()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(10)
User_Name = driver.find_element(By.NAME, "username")
User_Name.send_keys("student")
time.sleep(5)
PassWord = driver.find_element(By.NAME, "password")
PassWord.send_keys("Password123")
time.sleep(5)
Login = driver.find_element(By.ID, "submit")
Login.click()
time.sleep(10)
Actual_text = driver.title.title()
print(Actual_text)
Expected_text = "Logged In Successfully | Practice Test Automation"
if Expected_text == Actual_text:
    print("Login Successfully......")
else:
    print("Login Failed.... Try Again.")
driver.close()
