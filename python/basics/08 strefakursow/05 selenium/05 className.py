from selenium import webdriver
from selenium.webdriver.common.keys import Keys # biblioteka do obsługi klawiatury
from selenium.webdriver.common.by import By # do windows
import time

driver = webdriver.Chrome()

driver.get("https://www.python.org") 
search_form = driver.find_element(By.CLASS_NAME,'search-field') # szukamy naszego elementu po klasie, z której on korzysta( w przypadku gdy korzysta z wielu klas, wybieramy 1 - najczęściej rozdzielane są spacją) windows, ubuntu
# search_form = driver.find_element_by_class_name("search-field") # ubuntu
print("My search form element is: ")
print(search_form) # np(po każdym uruchomieniu otrzymamy inne Id): <selenium.webdriver.remote.webelement.WebElement (session="5e8d0e844a6bd294eed91aa3484acfb8", element="bd7fcc5a-731c-414a-bfd1-d76560df3836")>

search_form.clear() 
search_form.send_keys("Linux") 
search_form.send_keys(Keys.RETURN) 
search_form = driver.fullscreen_window()
time.sleep(10) 

search_form = driver.find_element(By.CLASS_NAME,'search-field')
search_form.clear()  
search_form.send_keys("drivers") 
search_form.send_keys(Keys.RETURN) 
search_form = driver.fullscreen_window()
time.sleep(10)

search_form = driver.find_element(By.CLASS_NAME,'search-field')
search_form.clear() 
search_form.send_keys("documentation") 
search_form.send_keys(Keys.RETURN) 
search_form = driver.fullscreen_window()
time.sleep(10)

driver.close()
search_form = driver.find_element
