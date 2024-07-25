"""
1. Open A browser
2. Open Orange Open Source site (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)
3. Login with details (Username : Admin Password : admin123)
4. Click Login
5. Capture the Home Page
6. Verify The Title OrangeHRM
7. Closed The Browser
"""

# "C:\\Users\\LENOVO\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
time.sleep(5)
new = driver.find_element(By.NAME, "search_query")
new.send_keys("Tere Vaaste")
time.sleep(2)
Click = driver.find_element(By.ID, "search-icon-legacy")
time.sleep(2)
Click.click()
Play = driver.find_element(By.CLASS_NAME, "yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded")
time.sleep(5)
Play.click()
# driver.find_element(ID, "search")
# driver1.find_element('submit').click()
time.sleep(10)


#############


