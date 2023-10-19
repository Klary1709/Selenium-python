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
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Firefox()
tiempo=2

'''
PRUEBA QA
tester: @Claribel Guardado
fecha 26/07/2023
'''

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
time.sleep(tiempo)

'''
SectDias=driver.find_element(By.XPATH,"//select[contains(@id,'select-demo')]")
#declaramos que es un selec para usar la libreria Select
ds=Select(SectDias)

ds.select_by_visible_text("Monday")
time.sleep(tiempo)
ds.select_by_index(1)
time.sleep(tiempo)
ds.select_by_value("Wednesday")
'''


time.sleep(tiempo)
driver.execute_script("window.scrollTo(0,500)")



ciudad=driver.find_element(By.ID,"multi-select")
sc=Select(ciudad)
#ciudad.send_keys(Keys.CONTROL)
actions = ActionChains(driver)

contador=0
'''

from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)

contador=0


actions.key_down(Keys.CONTROL)

uno=driver.find_element("xpath","//option[contains(text(),'New York')]").click()
dos=driver.find_element("xpath","//option[contains(text(),'New Jersey')]").click()
tres=driver.find_element("xpath","//option[contains(text(),'Washington')]").click()

'''


for i in range(6):
    #excluye
    if (i== 0 or i == 5 or i == 3):
        continue

    sc.select_by_index(i)
    contador=contador+1
    time.sleep(tiempo)


btnsec=driver.find_element("xpath","//button[contains(@id,'printAll')]").click()
time.sleep(tiempo)
btnsec2=driver.find_element("xpath","//button[contains(@id,'printMe')]").click()


print("contador: "+str(contador))
