from selenium import webdriver
from selenium.webdriver.common.keys import Keys # biblioteka do obsługi klawiatury
from selenium.webdriver.common.by import By # do windows
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(30) # jeśli strona ładuje się dłużej niż 30 sekund, wyrzzuci wyjątek
driver.get("http://www.strefakursow.pl/contact.html")
driver.fullscreen_window()

time.sleep(2)
driver.find_element(By.ID, "contact[full_name]").send_keys("Michał G")
time.sleep(2)
driver.find_element(By.ID, "contact[address]").send_keys("grabarzmichal@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "contact[subject]").send_keys("Selenium TEST")
time.sleep(2)
driver.find_element(By.ID, "contact[body]").send_keys("Test wypełniania\nformularza\nw Selenium!!!")
time.sleep(10)
driver.quit() # można użyć zamaist driver.close()

