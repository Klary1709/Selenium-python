import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
#POR ID

driver=webdriver.Firefox()

conta=0

for i in range (5):
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(2)


    nombre=driver.find_element("id","userName")
    nombre.send_keys("Marina")
    time.sleep(1)
    email=driver.find_element("id","userEmail")
    email.send_keys("Marina@yopmail.com")
    time.sleep(1)
    CAde=driver.find_element("id","currentAddress").send_keys("Direccion")
    time.sleep(1)
    PAdd=driver.find_element("id","permanentAddress").send_keys("Direccion 2")
    time.sleep(1)

    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(3)
    driver.find_element("id", "submit").click()


    time.sleep(4)
    driver.refresh()
    conta=conta+1