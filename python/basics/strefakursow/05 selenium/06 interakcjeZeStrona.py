from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By # do windows
import time

driver = webdriver.Chrome()

driver.get("https://www.strefakursow.pl")

element = driver.find_element(By.CLASS_NAME, "b-site-header__icon--login") # windows
element.click() # nie musimy użyć clear, click zrobi to automatycznie
driver.fullscreen_window()

time.sleep(5)

element2 = driver.find_element(By.ID, "customer_login")
element2.clear()
element2.send_keys("grabarzmichal@gmail.com")

time.sleep(5)

element3 = driver.find_element(By.ID, "customer_password")
element3.clear()
element3.send_keys("1910bioly")

time.sleep(5)

element3 = driver.find_element(By.ID, "js-login-button--submit")
element3.send_keys(Keys.RETURN)

time.sleep(15)

driver.close()
