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
T=2

class BaseUnitte(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test1(self):   
        d = self.driver
        f = FuncionesGlobales(d)
        #f.navegar("https://www.saucedemo.com/")
        f.texto_xpath("https://www.saucedemo.com/", "standard_user", "//input[contains(@id,'user-name')]", T)
        f.texto_id("secret_sauce", "password", T)
        f.dar_clic_by_id("//input[contains(@id,'login-button')]")


    def tearDown(self):
        d = self.driver
        d.close()


if __name__ == "__main__":
    unittest.main()
