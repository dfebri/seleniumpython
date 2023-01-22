from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class saucedemotest(unittest.TestCase):
 
    def test_login(driver):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click()    
        time.sleep(3)   

    def test_shoppingcart(driver):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click() 
        time.sleep(5)
        driver.find_element(By.ID, "shopping_cart_container").click() 
        time.sleep(5)

    def test_about(driver):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click() 
        driver.find_element(By.CLASS_NAME, "bm-burger-button").click() 
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "#about_sidebar_link").click() 
        time.sleep(5)

    def test_logout(driver):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click() 
        driver.find_element(By.CLASS_NAME, "bm-burger-button").click() 
        time.sleep(5)
        driver.find_element(By.ID, "logout_sidebar_link").click() 
        time.sleep(5)
        
if __name__ == "__main__":
    unittest.main()
