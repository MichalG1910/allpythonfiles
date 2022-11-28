from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://strefakursow.pl')

elem = driver.find_element_by_name("search_course[name]")
elem.clear()
elem.send_keys("docker")
elem.send_keys(Keys.RETURN)
time.sleep(10)

driver.close()