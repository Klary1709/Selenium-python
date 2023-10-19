import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from funciones import FuncionesGlobales 
from selenium.webdriver import ActionChains

import sys
d=""


@pytest.fixture(scope="function")
def setup_function(): 
    global d
    print("\n___________________\nINICIANDO  TEST")
    d=webdriver.Chrome()
    d.maximize_window()
    d.get("https://www.saucedemo.com/") 
    time.sleep(2)
    yield
    print("\n    FIN TEST    \n___________________")
    
    

def test_login1(setup_function):
    usser = d.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
    pas = d.find_element(By.XPATH, "//input[contains(@id,'password')]")
    btnSing = d.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

    usser.send_keys("Marina Guardado")
    pas.send_keys("Admin123")
    btnSing.click()

    AleError = d.find_element(By.XPATH, "//div[@class='error-message-container error']")
    time.sleep(2)

    error = AleError.text
    print("\nError: " + error)

    if (error== "Epic sadface: Username and password do not match any user in this service"):
        print("Los datos no son correctos")
        print("Prueba Uno OK")

def test_login2(setup_function):
    usser = d.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
    pas = d.find_element(By.XPATH, "//input[contains(@id,'password')]")
    btnSing = d.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

    usser.send_keys("Marina Guardado")
    # pas.send_keys("Admin123")
    btnSing.click()

    AleError = d.find_element(By.XPATH, "//div[@class='error-message-container error']")
    time.sleep(2)

    error = AleError.text
    print("\nMensaje de error : " + error)

    if error == "Epic sadface: Password is required":
        print("Falta la contraseña")
        print("Prueba  dos OK")

def test_login3(setup_function):
    usser = d.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
    pas = d.find_element(By.XPATH, "//input[contains(@id,'password')]")
    btnSing = d.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

    # usser.send_keys("Marina Guardado")
    pas.send_keys("Admin123")
    btnSing.click()

    AleError = d.find_element(By.XPATH, "//div[@class='error-message-container error']")
    time.sleep(2)

    error = AleError.text
    print("\nMensaje de error : " + error)

    if error == "Epic sadface: Username is required":
        print("Falta la nombre de usuario")
        print("Prueba tres OK")

def test_login4(setup_function):
    usser = d.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
    pas = d.find_element(By.XPATH, "//input[contains(@id,'password')]")
    btnSing = d.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

    # usser.send_keys("Marina Guardado")
    # pas.send_keys("Admin123")
    btnSing.click()

    AleError = d.find_element(By.XPATH, "//div[@class='error-message-container error']")
    time.sleep(2)

    error = AleError.text
    print("\nMensaje de error : " + error)

    if error == "Epic sadface: Username is required":
        print("Faltan ambos datos")
        print("Prueba cuatro OK")

def test_login5(setup_function):
    usser = d.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
    pas = d.find_element(By.XPATH, "//input[contains(@id,'password')]")
    btnSing = d.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

    usser.send_keys("standard_user")
    pas.send_keys("secret_sauce")
    btnSing.click()
    time.sleep(4)

    carico = d.find_element(By.XPATH, "//a[contains(@class,'shopping_cart_link')]")
    print(carico.is_displayed())
    print("Logeo exitoso")
    print("Prueba cinco OK")


if __name__ == "__main__":
    pytest.main()
    