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
        
        f.navegar("https://demoqa.com/buttons")
        
        # btnDobleclic=d.find_element(By.XPATH,"//button[contains(@id,'doubleClickBtn')]")
        # acciones=ActionChains(d)
        # acciones.double_click(btnDobleclic).perform()
        
        f.clicdoble_mixto("XPATH","//button[contains(@id,'doubleClickBtn')]")
        
 
                

    def tearDown(self):
        d = self.driver
        #d.close()


if __name__ == "__main__":
    unittest.main()


# > python -m PRACTCA2.Practica1uni
