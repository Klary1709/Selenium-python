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
from FUNCIONES.funcionesexc import FuncionesExc
from FUNCIONES.PAGE_LOGIN  import PageLogin
T=.2

class BaseUnitte(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test1(self):
        d=self.driver
        f=FuncionesGlobales(d)
        fe=FuncionesExc(d)
        f.navegar("https://demoqa.com/text-box")
        ruta="C:\\Users\Claribel\PycharmProjects\HolaMundoChrome\IMAGENES\DOCUMENTOS\exel.xlsx"
        filas=fe.getRowCount(ruta,"Hoja1")
        
        #col
        for i in range(2,filas+1):
            nombre=fe.readData(ruta,"Hoja1",i,1)
            email=fe.readData(ruta,"Hoja1",i,2)
            dir1=fe.readData(ruta,"Hoja1",i,3)
            dir2=fe.readData(ruta,"Hoja1",i,4)

            #leyendo info
            f.texto_mixto("xpath",nombre,"//input[contains(@id,'userName')]",T)
            f.texto_mixto("xpath",email,"//input[contains(@id,'userEmail')]",T)
            f.texto_mixto("xpath",dir1,"//textarea[contains(@id,'currentAddress')]",T)
            f.texto_mixto("xpath",dir1,"//textarea[contains(@id,'permanentAddress')]",T)
            f.clic_mixto("xpath","//button[contains(@id,'submit')]")
            f.tiempo(1)
        
            #Escribiendo en el excel
            e=f.existe("xpath","//p[@id='name']")
            if(e=="Existe"): 
                print("El elemento se inserto corretamente\n")
                fe.writeData(ruta,"Hoja1",i,5,"INSERTADO")
            else:
                print("El elemento se NO SE INSERTO corretamente\n")
                fe.writeData(ruta,"Hoja1",i,5,"NO INSERTADO")
                 
            
            
        
    def tearDown(self):
        d = self.driver
        d.close()


if __name__ == "__main__":
    unittest.main()
