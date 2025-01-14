# Importing necessary libraries
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Initialize the WebDriver
services = Service("C:\\Users\\LENOVO\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services,options=options)

# Navigate to FitPeo Homepage
driver.get('https://careers.valuelabs.com/')
driver.maximize_window()
driver.implicitly_wait(5)

driver.execute_script('window.scrollBy(100,0)')
Job_title = driver.find_element(By.ID, 'show-role')
Job_title.send_keys("Quality Engineer")

Location = driver.find_element(By.ID, 'show-location')
Location.send_keys('Hyderabad')

time.sleep(4)
Serach = driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div/form/fieldset/div/button')
Serach.click()

time.sleep(10)