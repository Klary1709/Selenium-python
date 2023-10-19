'''
DOCUMENTACION : https://selenium-python.readthedocs.io/waits.html
'''

import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
tiempo=4

'''
PRUEBA QA
tester: @Claribel Guardado
fecha 26/07/2023
'''

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
time.sleep(tiempo)

btn1=WebDriverWait(driver,10).until(EC.element_to_be_clickable(("xpath","//body/div[@id='easycont']/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/label[1]")))
btn1.click()
#btn1=driver.find_element("xpath","//body/div[@id='easycont']/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/label[1]").click()

btn2=WebDriverWait(driver,10).until(EC.element_to_be_clickable(("xpath","//label[contains(.,'Option 2')]")))
btn2.click()

btn3=WebDriverWait(driver,10).until(EC.element_to_be_clickable(("xpath","//label[contains(.,'Option 4')]")))
btn3.click()
