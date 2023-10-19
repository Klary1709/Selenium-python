import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from FUNCIONES.funciones import FuncionesGlobales
from selenium.webdriver import ActionChains
import sys

"""
Function -> Function, My_function
Variable -> x, var, myVariable
Class    -> Model, MyClass
Method   -> class_method, method
Constant ->  CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT
"""

class base_test(unittest.TestCase): 
    
    def setUp(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window() 
        t=2
    
    def test1(self): 
        d= self.driver
        f=FuncionesGlobales(d) 
        # f.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # f.texto_mixto("XPATH","admin","//input[contains(@name,'username')]",2)
        # f.texto_mixto("XpATH","admin123","//input[contains(@name,'password')]",2)
        # f.clic_mixto("xpath","//button[@type='submit']",2)
        
        # resutado=f.existe("xPath","//i[@class='oxd-icon bi-question-lg']")
        # if(resutado=="existe"):
        #     print("El usuario se ha logeado con exito")
        # else:
        #     print("El logeo a fallado ")
        
        f.navegar("https://testingqarvn.com.es/")
        practica=d.find_element(By.XPATH,"(//a[@href='https://testingqarvn.com.es/practicas-qa/'])[1]")
        combox_opc=d.find_element(By.XPATH,"(//a[@href='https://testingqarvn.com.es/combobox/'][contains(.,'ComboBox')])[1]")
        upload_opc=d.find_element(By.XPATH,"(//a[@href='https://testingqarvn.com.es/upload-files/'][contains(.,'Upload Files')])[1]")
        
        accion=ActionChains(d)
        #si uso el move_to_element se hace pero no se ve graficamente si anexamos el perform() se ve 
        accion.move_to_element(practica).move_to_element(combox_opc).click().perform()

        
                

    def tearDown(self):
        d = self.driver
        #d.close()


if __name__ == "__main__":
    unittest.main()


# > python -m PRACTCA2.Practica1uni
