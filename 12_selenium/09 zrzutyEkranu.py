from selenium import webdriver
from selenium.webdriver.common.keys import Keys # biblioteka do obsługi klawiatury
from selenium.webdriver.common.by import By # do windows
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(30) # jeśli strona ładuje się dłużej niż 30 sekund, wyrzzuci wyjątek
driver.get("https://www.facebook.com")
driver.maximize_window() # pełny ekran przez cas działania skryptu
driver.implicitly_wait(20) # pwrdpd czas jaki oczekuje program na wczytanie odpowiedniego elementu(po tym czasie wyrzuci wyjątek). Umieszczamy go tylko raz na cały skrypt
driver.find_element(By.CLASS_NAME, "_9xo7").click()
time.sleep(1)

driver.get_screenshot_as_file("./Facebook.png")
driver.find_element(By.ID, "email").send_keys("grabarzmichal@gmail.com")
time.sleep(3)
driver.find_element(By.NAME, "pass").send_keys("HASŁO")
time.sleep(3)
driver.find_element(By.NAME, "login").click()
time.sleep(1)
driver.get_screenshot_as_file("./Facebook1.png")
driver.quit()
