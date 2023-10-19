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




driver=webdriver.Firefox()
tiempo=2


driver.maximize_window()
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
time.sleep(tiempo)

'''
    
    NO SE PUEDE USAR ESTO EN EL TRY EXCEP sino usando el WebDriverWait
    
    selec1=driver.find_element("xpath","//select[@id='select-demoAAA']")
    dias=Select(selec1)
    dias.select_by_value("Sunday")
    ti
me.sleep(1)
    dias.select_by_index(2)
    time.sleep(1)
    dias.select_by_visible_text("Monday")
    time.sleep(1)

'''
try:
    #PARA QUE FUNCIONEN EK EXCEOP SE DEBE USAR UN expected_conditions en este caso es EC que es para que se corrobore que esta el elemento

    #aqui solo corrobora que se encuentre el elemento
    diaSelect=WebDriverWait(driver,10).until(EC.visibility_of_element_located(("xpath","//select[@id='select-demo']")))
    days=Select(diaSelect)
    days.select_by_visible_text("Sunday")
    time.sleep(1)
    days.select_by_index(2)
    time.sleep(1)
    days.select_by_visible_text("Monday")
    time.sleep(1)

except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

#Si hay un error solo cierra el navegador
'''

finally:
    driver.quit()
'''
driver.execute_script("window.scrollTo(0,500)")

ciudad=Select(driver.find_element(By.ID, "multi-select"))
ciudad.select_by_index(1)
time.sleep(1)
ciudad.select_by_index(2)
time.sleep(1)
ciudad.select_by_index(5)
time.sleep(1)