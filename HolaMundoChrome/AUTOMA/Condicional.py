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
driver.get("https://demoqa.com/")
time.sleep(4)

titulo=driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
btn1=driver.find_element(By.XPATH,"(//div[contains(@class,'card-up')])[1]")

if(titulo.is_displayed()==True):
    print("Estanos en la pagina principal")
    btn1.click()
    time.sleep(3)
else: 
    print("No estamos en la pagina principal ")

time.sleep(4)
driver.close()
