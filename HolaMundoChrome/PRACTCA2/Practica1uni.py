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


class PruebaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        d = self.driver

    def test_login1(self):
        d = self.driver
        f = FuncionesGlobales(d)
        f.saludo()

    def tearDown(self):
        d = self.driver
        d.close()


if __name__ == "__main__":
    unittest.main()
