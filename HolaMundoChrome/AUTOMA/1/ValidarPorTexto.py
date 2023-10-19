import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert



driver=webdriver.Firefox()

driver.maximize_window()
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
time.sleep(4)

 
try:
    #si quiero que se use try excep  es webdriverawait 
    btnEnviar=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit'][contains(.,'Send')]")))
    btnEnviar2=driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Send')]")
    #vamos=driver.execute_script("arguments[0].scrollIntoView();", btnEnviar)
    btnEnviar.click()

    name_val=driver.find_element(By.XPATH,"//small[@class='help-block'][contains(.,'Please supply your first name')]")
    name=name_val.text
    if(name=="Please supply your first name"): 
        cd=driver.find_element(By.XPATH,"//input[contains(@name,'first_name')]")
        cd.send_keys("Marina Cl")
        time.sleep(1)
        print("Nombre Correcto")
    else:
        print("Falta Nombre")

#APELLIDO
    name_ap=driver.find_element(By.XPATH,"//small[@class='help-block'][contains(.,'Please supply your last name')]")

    nameap=name_ap.text

    if(nameap=="Please supply your last name"): 
        cd=driver.find_element(By.XPATH,"//input[contains(@name,'last_name')]")
        cd.send_keys("Guardado Monge")
        time.sleep(1)
        print("Apellido Correcto")
    else:
        print("Falta Apellido ")

    if(btnEnviar2.is_enabled==True):
        print("Formulario lleno")
    else: 
        print("Faltan campos  ")

except TimeoutException as ex: 
    print("Ah ocurrido un error ")


time.sleep(4)
driver.close()
