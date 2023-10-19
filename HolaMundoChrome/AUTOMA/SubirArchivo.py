
#DOCUMENTACIÓN : https://selenium-python.readthedocs.io/waits.html



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
driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
time.sleep(2)
#with open("../IMAGENES/hola.txt","r") as file:
#    print(file.read())

try:
    #aqui solo corrobora que se encuentre el elemento
    CargarArch=WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='fileinput']")))
    #PARA QUE FUNCIONEN EK EXCEOP SE DEBE USAR UN expected_conditions en este caso es EC.
    CargarArch = driver.find_element(By.XPATH,"//input[@id='fileinput']")
    #solo se debe poner doble fleca al inicio
    #CargarArch.send_keys("C:\\Users\Claribel\PycharmProjects\HolaMundoChrome\IMAGENES\ArchSub.jpg")
    #se puede solo usar r y "" para no ser necesario el donle slash
    CargarArch.send_keys(r"C:\Users\Claribel\PycharmProjects\HolaMundoChrome\IMAGENES\ArchSub.jpg")

    esImg=driver.find_element(By.XPATH,"//input[@id='itsanimage']")
    esImg.click()

    time.sleep(4)

    btnSubir=driver.find_element(By.XPATH,"//input[contains(@type,'submit')]")
    btnSubir.click()

    time.sleep(2)


except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")











