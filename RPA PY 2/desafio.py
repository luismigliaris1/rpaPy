from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()

navegador.get("https://www.rpachallenge.com/")
tempoEspera.sleep(2)

#name
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys("Luis")
tempoEspera.sleep(2)

#lastName
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys("Migliaris")
tempoEspera.sleep(2)

#email
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys("luishencm2@hotmail.com")
tempoEspera.sleep(2)

#role in company
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys("Nada")
tempoEspera.sleep(2)

#adress
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys("SJRP")
tempoEspera.sleep(2)

#phoneNumber
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys("9999999999")
tempoEspera.sleep(2)

#companyName
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys("Luis")
tempoEspera.sleep(2)

navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
tempoEspera.sleep(2)


