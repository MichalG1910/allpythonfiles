from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("https://strefakursow.pl/")

element = driver.find_element_by_class_name('b-site-header__bottom-login-button')
element.click() # klikamy clear -> czysci elementy typu input text itp.

time.sleep(10)

element2 = driver.find_element_by_id('customer_login')
element2.clear() # dobrze jest wyczyscic by miec pewnosc że wpisuje sie swoje
element2.send_keys('email@domena.pl')

time.sleep(10)

element3 = driver.find_element_by_id('customer_password')
element3.clear()
element3.send_keys('PASSWORD')

time.sleep(10)

element3.send_keys(Keys.RETURN)
time.sleep(3)

driver.close()