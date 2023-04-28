from selenium import webdriver
from selenium.webdriver import ActionChains # odpowiada za prace na formach/warstwach w metodzie Drag and Drop
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://jqueryui.com/droppable")
driver.fullscreen_window()

driver.switch_to.frame(0) # przełączamy się na warstwę (0)

action_chains = ActionChains(driver) # tworzymy nasz obiekt i podpinamy do niego sterownik (nasza warstwa)

source = driver.find_element(By.ID, "draggable") # tworzymy element (obiekt), którym będziemy mogli ruszać
target = driver.find_element(By.ID, "droppable") # tworzymy element (obiekt) nieruchomy, który będzie celem, na który będziemy upuszczać nasz obiekt source
time.sleep(3)

action_chains.drag_and_drop_by_offset(source, 100, 100).perform() # nasza akcja- przesuwamy obiekt source o 100 pikseli w poziomie i 100 w pionie
time.sleep(3)

action_chains.drag_and_drop(source, target).perform() # nasza 2 akcja - obiekt source przesuwamy na nasz target (naz cel)
time.sleep(10)

driver.close()


