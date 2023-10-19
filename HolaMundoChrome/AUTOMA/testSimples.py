import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()

driver.get("https://marn.ventanilla.simple.sv/")
driver.maximize_window()
time.sleep(2)
#Seleecion ciudadano
SelectID=driver.find_element("xpath","//select[@id='provider']").click()
#opcFunc=driver.find_element("xpath","//option[contains(text(),'Login Funcionario')]").click()
opcCiudadano=driver.find_element("xpath","//option[contains(text(),'Identidad Digital')]").click()

iniciarSeccionID=driver.find_element("xpath","//body/div[@id='app']/nav[1]/div[1]/div[1]/ul[1]/form[1]/li[2]/button[1]").click()

#Redireccion a login IDENTIDAD DIGUITAL

user=driver.find_element("xpath","//input[@id='email']").send_keys("05800174-1")

#passt=driver.find_element("xpath","//input[@id='password']").send_keys("Admin123_")
passt=driver.find_element(By.ID,"password").send_keys("Admin123_")

clicbot=driver.find_element("xpath","//button[contains(text(),'Iniciar Sesión')]").click()



#SELECCIONANDO EL TRAMITE
iniciTrami=driver.find_element("xpath","//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
btnSif=driver.find_element(By.XPATH,"//button[contains(text(),'Siguiente')]").click()





