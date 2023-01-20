from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class login(unittest.TestCase):

    def set_login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        # self.driver.find_element(By.LINK_TEXT,"Login").click()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click() 
        # self.driver.find_element(By.NAME, value= "login").click()        
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
