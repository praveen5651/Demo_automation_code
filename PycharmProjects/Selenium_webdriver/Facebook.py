from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/?stype=lo&jlou=Afdsx_qm8LUiFqpRefZdY0dwSWgFgmrlf5B7eWlmbmAbR6ORzt8W8dHL6XM6Y8wuhi_uGjAFqLwUjPZtyUvpKoh7gNoEsSlwk4bjSemQhim3dw&smuh=64453&lh=Ac-E5gf67wc55uWI8ds")
time.sleep(5)
user = driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("praveen@gamil.com")
pwd = driver.find_element(By.ID, "pass").send_keys("12345")
time.sleep(2)
sub = driver.find_element(By.NAME, "login").click()
time.sleep(5)
driver.quit()