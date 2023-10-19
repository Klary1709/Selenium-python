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

btnEnviar=driver.find_element(By.XPATH,"//button[contains(@id,'submit')]")
#vamos=driver.execute_script("arguments[0].scrollIntoView();", btnEnviar)

print(btnEnviar.is_enabled())
if(btnEnviar.is_enabled==True): 
    print("Puedes dar click")
else: 
    print("No puedes dar click")


time.sleep(4)
driver.close()
