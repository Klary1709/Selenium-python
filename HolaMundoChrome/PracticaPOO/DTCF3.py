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

    def test1(self):
        d=self.driver
        f=FuncionesGlobales(d)
        pl=PageLogin(d)
        print("A")
        #Login SELECCION CIUDADANO }
        f.navegar("https://vuc.egob.sv/")
        pl.iniciarCiudadano("05800174-1","Admin123_")
        f.tiempo(2)

        #f.clic_mixto("xPatH","(//a[contains(@class,'card-footer claveunica')])[174]")  
        f.navegar("https://vuc.egob.sv/etapas/ejecutar/137386")
        #f.clic_mixto("xpath","//a[@href='https://dtc.ventanilla.simple.sv/etapas/ejecutar/3002731'][contains(.,'Realizar')]")
        f.tiempo(4)
        f.clic_mixto("xpath","(//span[contains(.,'Seleccionar')])[1]")       
        #usando el XY
        f.clicXY("xpath","(//span[contains(.,'Seleccionar')])[1]",0,150,5)
        #usando seteo
        f.clic_mixto("xpath","(//span[contains(.,'Seleccionar')])[1]")    
        texto= f.SEXP("(//input[contains(@class,'chosen-search-input')])[1]")
        texto.send_keys("Primera vez"+Keys.ENTER)    
        f.tiempo(10)
        
        
        
    
        
        
        
        
        
        
        
        
        
     
    def tearDown(self):
        d = self.driver
        d.close()


if __name__ == "__main__":
    
    unittest.main()
