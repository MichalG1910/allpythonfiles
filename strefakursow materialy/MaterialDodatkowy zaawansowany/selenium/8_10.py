from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("./Facebook.png")
driver.find_element_by_id("email").send_keys("strefakursow@kurs.pl")
driver.find_element_by_name("pass").send_keys("KursPython")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("./Facebook1.png")
driver.quit()