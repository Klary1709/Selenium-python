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
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
time.sleep(4)


driver.find_element(By.XPATH,"//a[@href='#myModal0']").click()
time.sleep(4)
# Alert(driver).accept()
# Alert(driver).dismiss()
try: 
    Buscar=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]")))
    Buscar=driver.find_element(By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]").click()
except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

time.sleep(4)
driver.close()
