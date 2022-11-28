from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.set_page_load_timeout(30)
driver.get("https://strefakursow.pl/contact.html")

driver.find_element_by_id('contact[full_name]').send_keys('Piotr')
driver.find_element_by_id('contact[address]').send_keys('piotr@ja.pl')
driver.find_element_by_id('contact[subject]').send_keys('Kurs Python')
driver.find_element_by_id('contact[body]').send_keys('Tu wpis na kilka \n Lini :) \n tu kolejna')
time.sleep(10)
driver.quit()
