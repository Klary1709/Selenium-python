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

driver.maximize_window()
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
time.sleep(2)

#oBTENER TODOS LOS LINKS DE LA PAG

links=driver.find_elements(By.TAG_NAME,"a")

print("El numero numero de links que hay en la pag es: ",len(links))


for i in links:
    print(i.text)

driver.find_element(By.LINK_TEXT,"Date pickers").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT,"JQuery Date Picker").click() 
time.sleep(2)




# try:
#     nom=driver.find_element(By.XPATH,"//input[contains(@name,'first_name')]")
#     nom.send_keys("Marina Claribel")

#     ape=driver.find_element(By.XPATH,"//input[contains(@name,'last_name')]")
#     ape.send_keys("Guaradado Monge")


#     llenadoAtab=driver.find_element(By.XPATH,"//input[contains(@name,'email')]")
#     llenadoAtab.send_keys("Marina@gmail.com"+Keys.TAB+
#                           "8455555122"+Keys.TAB+
#                           "Acajutla, Res Magdoli"+Keys.TAB+
#                           "Sonsonate"+Keys.TAB
#                           )
#     Satate=driver.find_element(By.XPATH, "//select[contains(@name,'state')]")
#     selec=Select(Satate)
#     selec.select_by_index(10)
#     time.sleep(3)

#     llenadoAtab2=driver.find_element(By.XPATH,"//input[contains(@name,'zip')]")
#     llenadoAtab2.send_keys("66013"+Keys.TAB+
#                           "www.miwebsite.com"+Keys.TAB+
#                           "La descripción del proyexto "+Keys.TAB+
#                           "Sonsonateonsonateonsonateonsonate"+Keys.TAB)
#     time.sleep(3)


#     hostbtn=driver.find_element(By.XPATH,"//input[contains(@value,'yes')]")
#     hostbtn.click()
#     time.sleep(3)

#     sendbtn=driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Send')]")
#     sendbtn.click()

# except TimeoutException as ex:
#     print(ex.msg)
#     print("Elemento no disponible")










