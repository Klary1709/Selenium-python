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
driver.get("https://marn.ventanilla.simple.sv/")
time.sleep(2)


try:
    nom=driver.find_element(By.XPATH,"//a[@href='https://marn.ventanilla.simple.sv/login/claveunica?redirect=https://marn.ventanilla.simple.sv/tramites/iniciar/224&provider=16'][contains(.,'Iniciar con Identidad Digital                                                                                                                            →')]")
    nom.send_keys("Marina Claribel")

    ape=driver.find_element(By.XPATH,"//input[contains(@name,'last_name')]")
    ape.send_keys("Guaradado Monge")


    llenadoAtab=driver.find_element(By.XPATH,"//input[contains(@name,'email')]")
    llenadoAtab.send_keys("Marina@gmail.com"+Keys.TAB+
                          "8455555122"+Keys.TAB+
                          "Acajutla, Res Magdoli"+Keys.TAB+
                          "Sonsonate"+Keys.TAB
                          )
    Satate=driver.find_element(By.XPATH, "//select[contains(@name,'state')]")
    selec=Select(Satate)
    selec.select_by_index(10)
    time.sleep(3)

    llenadoAtab2=driver.find_element(By.XPATH,"//input[contains(@name,'zip')]")
    llenadoAtab2.send_keys("66013"+Keys.TAB+
                          "www.miwebsite.com"+Keys.TAB+
                          "La descripción del proyexto "+Keys.TAB+
                          "Sonsonateonsonateonsonateonsonate"+Keys.TAB)
    time.sleep(3)


    hostbtn=driver.find_element(By.XPATH,"//input[contains(@value,'yes')]")
    hostbtn.click()
    time.sleep(3)

    sendbtn=driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Send')]")
    sendbtn.click()

except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")
