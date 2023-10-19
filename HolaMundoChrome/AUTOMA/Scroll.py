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
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



driver=webdriver.Firefox()
tiempo=2

driver.maximize_window()
driver.get("https://pixabay.com/es/")
time.sleep(2)
"""
try:
    #aqui solo corrobora que se encuentre el elemento
    CargarArch=WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='fileinput']")))


except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

"""
#AL CALCULO
"""driver.execute_script("window.scrollTo(0,100)")"""
#LA FORMA CORRECTA ES

try:
    btnDescubreMas=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    btnDescubreMas=driver.find_element(By.XPATH,"//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    imgdentrodeboton=driver.find_element(By.XPATH,"//body/div[@id='app']/div[1]/div[2]/div[1]/div[2]/div[2]")
    #ir=driver.execute_script("arguments[0].scrollInToView();",btnDescubreMas)
    vamos=driver.execute_script("arguments[0].scrollIntoView();", imgdentrodeboton)



    time.sleep(5)
    btnDescubreMas.click()

except TimeoutException as ex:
    print(ex.msg)
    print("NO SE HA ENCONTRADO ELEMENTO DISPONIBLE")









