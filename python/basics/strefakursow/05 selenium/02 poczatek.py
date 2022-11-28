from selenium import webdriver
from selenium.webdriver.common.keys import Keys # biblioteka do obsługi klawiatury
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox() # wybieramy przeglądarke
driver.get("https://www.python.org") # przekazujemy adres www - przeglądarka uruchomi się w tryie testów
# elem = driver.find_element_by_name("q") # tworzymy obiekt z elementem strony www (q - na python.org jet to wyszukiwarka zawartości strony) ubuntu
# elem = driver.find_element("name","q") # tworzymy obiekt z elementem strony www (q - na python.org jet to wyszukiwarka zawartości strony) windows (działa też na ubuntu)
elem = driver.find_element(By.NAME, "q") # By-uniwersalna metoda(ubuntu, windos- pamiętaj o imporcie biblioteki)
# driver.get("https://www.strefakursow.pl") # to samo co wyżej tylko dla innej strony
# elem = driver.find_element_by_name("search_course[name]") 

# find_element_by_name("q") - szukanie interesującego nas elementu strony www - otwierasz www --> PrawyPrzyciskMyszy(PPM) --> Zbadaj(Chrome,Firefox)
# otwiera się narzędzie DevTools, w lewym górnym rogu ikona okienko+kursor. Najeżdżasz na element strony www i podświetla ci kod
# danego elementu. Interesuje cię "name" czyli nazwa. 


elem.clear() # czyścimy element (naszą wyszukiwarkę) 
elem.send_keys("pycon") # przesyłamy do naszego elementu(wyszukiwarki) string - zostanie on wpisany do wyszukiwania
elem.send_keys(Keys.RETURN) # potwierdzamu nasz wyraz klawiszem return(by uruchomić wyszukiwanie)
time.sleep(10) # uśpimy skrypt na 10 sekund

driver.close() # zamykamy naszą przeglądarkę