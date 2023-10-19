from selenium import webdriver
from selenium.webdriver.common.keys import  Keys

#una variable que nos permitira ejecutar el drive en el navegador
driver= webdriver.Chrome()

#pasamos el sitio donde haremos la automatización
driver.get("https://demoqa.com/text-box")
print("Primera prueba qa automatizada")
print(driver.title)

driver.close()
