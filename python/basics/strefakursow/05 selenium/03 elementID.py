from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.python.org") 
# search_form = driver.find_element("id", 'id-search-field') # szukamy naszego elementu po Id (ubuntu, windows)
# search_form = driver.find_element_by_id('id-search-field') # szukamy naszego elementu po Id (tylko ubuntu)
search_form = driver.find_element(By.ID, 'id-search-field') 
print("My search form element is: ")
print(search_form) # np(po każdym uruchomieniu otrzymamy inne Id): <selenium.webdriver.remote.webelement.WebElement (session="5e8d0e844a6bd294eed91aa3484acfb8", element="bd7fcc5a-731c-414a-bfd1-d76560df3836")>

search_form.clear() 
search_form.send_keys('linux') 
search_form.send_keys(Keys.RETURN)
search_form = driver.fullscreen_window() 
time.sleep(10) 

search_form = driver.find_element(By.ID, 'id-search-field') 
search_form.clear() 
search_form.send_keys("drivers") 
search_form.send_keys(Keys.RETURN) 
search_form = driver.fullscreen_window()
time.sleep(10)

search_form = driver.find_element(By.ID, 'id-search-field') 
search_form.clear() 
search_form.send_keys("documentation") 
search_form.send_keys(Keys.RETURN) 
search_form = driver.fullscreen_window()
time.sleep(10)

driver.close()
