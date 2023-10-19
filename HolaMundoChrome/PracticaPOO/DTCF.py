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
        self.driver = webdriver.Chrome()

    def test1(self):
        d=self.driver
        d.get("https://dtc.ventanilla.simple.sv/tramites/informativo/250")
        # f=FuncionesGlobales(d)
        # pl=PageLogin(d)
        # print("A")
        # Login SELECCION CIUDADANO 
        # pl.iniciarCiudadano("https://dtc.ventanilla.simple.sv/tramites/informativo/250","05800174-1","Admin123_")
        # f.tiempo(2)
        # print("uno")
        # f.navegar("https://dtc.ventanilla.simple.sv/etapas/ejecutar/2967049")
        
                
        # pl.selector_simples_ccselector("#regiones_567504_chosen"
        #                     ,"Sonsonate")
        
    
        
        
        
        
        
        
        
        
        
     
    def tearDown(self):
        d = self.driver
        #d.close()


if __name__ == "__main__":
    
    unittest.main()
