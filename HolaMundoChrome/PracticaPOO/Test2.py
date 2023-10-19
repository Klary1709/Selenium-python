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
        #d.get("https://www.saucedemo.com/")
        pl=PageLogin(d)
        pl.login_master("https://www.saucedemo.com/",
                        "standard_user","//input[contains(@id,'user-name')]",
                        "secret_sauce","password",
                        "//input[contains(@id,'login-button')]",T
                        )
        
    def tearDown(self):
        d = self.driver
        d.close()


if __name__ == "__main__":
    unittest.main()
