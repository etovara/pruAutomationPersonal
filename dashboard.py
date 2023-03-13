from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


#URL
driver = webdriver.Chrome(executable_path= r"C:\Users\Edwin Tovar\Desktop\pruAutomationPersonal\chromedriver\chromedriver.exe")
driver.get("https://www.personal.com.ar/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)

#Hacer Zoom a una Pagina
#driver.execute_script("document.body.style.zoom='80%'")
#time.sleep (3)

#Scroll Down / Up
#Se puede realizar Pixeles o de acuerdo al tamaño vertical de la pagina
#Mediante Pixeles
#driver.execute_script("window.scrollBy(0, 6000);")
#time.sleep(2)
#driver.execute_script("window.scrollBy(0, -6000);")
#time.sleep(2)

#Mediante Tamaño Vertical de la pagina
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep (2)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
time.sleep (2)

#Combos
combos = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div[2]/section/div/ul/li[1]/a/div/i')
ActionChains(driver).move_to_element(combos).click(combos).perform()
time.sleep(3)

#Regreso a la pagina principal de personal
personal = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[1]/teco-preheader/div/div/div[1]/div/teco-button[1]/a')
ActionChains(driver).move_to_element(personal).click(personal).perform()
time.sleep(3)

#Tienda
tienda = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div[2]/section/div/ul/li[2]/a/div/i')
ActionChains(driver).move_to_element(tienda).click(tienda).perform()
time.sleep(3)

#Regreso a la pagina principal de personal
personal = driver.find_element(By.XPATH, '//*[@id="materialize-framework"]/teco-preheader/div/div/div[1]/div/a[1]')
ActionChains(driver).move_to_element(personal).click(personal).perform()
time.sleep(3)

#Internet
internet = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div[2]/section/div/ul/li[3]/a/div/i')
ActionChains(driver).move_to_element(internet).click(internet).perform()
time.sleep(3)

#Regreso a la pagina principal de personal
personal = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[1]/teco-preheader/div/div/div[1]/div/teco-button[1]/a')
ActionChains(driver).move_to_element(personal).click(personal).perform()
time.sleep(3)

#Planes
planes = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div[2]/section/div/ul/li[4]/a/div/i')
ActionChains(driver).move_to_element(planes).click(planes).perform()
time.sleep(3)

#Regreso a la pagina principal de personal
personal = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[1]/teco-preheader/div/div/div[1]/div/teco-button[1]/a')
ActionChains(driver).move_to_element(personal).click(personal).perform()
time.sleep(3)

#Portabilidad
portabilidad  = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div[2]/section/div/ul/li[5]/a/div/i')
ActionChains(driver).move_to_element(portabilidad).click(portabilidad).perform()
time.sleep(3)

#Regreso a la pagina principal de personal
personal = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[1]/teco-preheader/div/div/div[1]/div/teco-button[1]/a')
ActionChains(driver).move_to_element(personal).click(personal).perform()
time.sleep(3)

#Tv y Streaming
tvyStreaming = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div[2]/section/div/ul/li[6]/a/div/span/img') 
ActionChains(driver).move_to_element(tvyStreaming).click(tvyStreaming).perform()
time.sleep(3)

#Regreso a la pagina principal de personal
personal = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/div[1]/teco-preheader/div/div/div[1]/div/teco-button[1]/a')
ActionChains(driver).move_to_element(personal).click(personal).perform()
time.sleep(3)

#Cierro Navegador
driver.close()