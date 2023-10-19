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
from FUNCIONES.PAGE_LOGIN  import PageLogin
T=2

class BaseUnitte(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        print("Estamos en funciones TEST2")

    def test1(self):
        d=self.driver
        f=FuncionesGlobales(d)
        #f.navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        #f.navegar("https://demo.seleniumeasy.com/input-form-demo.html")
        f.navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
        f.tiempo(4)
        #f.select_xpath_text("//select[contains(@id,'select-demo')]", "Monday")
        #f.select_id_type("select-demo","index", "3")
        #f.subirarch_xpath("C:\\Users\Claribel\PycharmProjects\HolaMundoChrome\IMAGENES\ArchSub.jpg","//input[contains(@id,'fileinput')]")
        #f.subirarch_xpath("//input[contains(@id,'fileinput')]")
        #f.dar_clic_by_xpth("//label[contains(.,'Option 2')]")
        #f.dar_clic_by_xpth("//label[contains(.,'Option 3')]")
        # for num in range(0,3): 
        #     f.ccheckmultiple("//body/div[@id='easycont']/div[1]/div[2]/div[2]/div[2]/div["+str(num)+"]")
            
        #     #f.checkmultiple("//label[contains(.,'Option "+str(num)+"')]")
        #f.texto_mixto("xpath","Marina","//input[contains(@name,'first_name')]")
        f.clic_mixto("id","isAgeSelected")
        f.tiempo(10)
        
        
        

    def tearDown(self):
        d = self.driver
        d.close()


if __name__ == "__main__":
    unittest.main()
