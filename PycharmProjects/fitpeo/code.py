from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

class TestFitpeoPage(unittest.TestCase):
    def setUp(self):
        self.service = Service("C:\\Users\\LENOVO\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.fitpeo.com/")
        self.driver.maximize_window()
        # self.driver.switch_to.frame()

    def test_page_title(self):
        self.assertTrue("Fitpeo" in self.driver.title, "Title does not contain 'Fitpeo'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
