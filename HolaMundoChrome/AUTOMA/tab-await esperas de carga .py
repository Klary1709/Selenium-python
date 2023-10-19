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

#desde que carge la pag le dara 13 segundo para que carge
'''
driver.implicitly_wait(13)
'''
#desde que carge la pag le dara 13 segundo para que carge
'''
                                            el elemento sea cliqueable 
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "myDynamicElement"))
elecment.click()
'''



driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(tiempo)

#podemos usar el or o el and al igual que los ciclos repetitivos
nom=driver.find_element(By.XPATH,"//input[@id='userName']" ) and driver.find_element(By.CSS_SELECTOR,"#userName" )
#nom=driver.find_element("xpath","//input[@id='userName']")
nom.send_keys("Marina Claribel Guardado")
nom.send_keys(Keys.TAB + "MarinaGuardado@yopmail.com" +Keys.TAB + "Direccion 1" + Keys.TAB +"Direccion 2" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(tiempo)

driver.find_element("xpath","//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]").click()
time.sleep(tiempo)

#regresar
#driver.back()

driver.execute_script("window.history.go(-1)")
time.sleep(tiempo)


driver.close()