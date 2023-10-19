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

from selenium.webdriver.chrome.options import Options
import sys
d=""

@pytest.fixture(scope="function")
def setup_function(): 
    global d
    print("\n___________________\nINICIANDO  TEST")
    f=FuncionesGlobales(d) 
    d=webdriver.Firefox()
    d.maximize_window()
    d.get("https://google.com") 

    
    
    time.sleep(2)
    yield
    print("\n    FIN TEST    \n___________________")
 
 
def test1(setup_function):
    f=FuncionesGlobales(d)
    acciones=ActionChains(d)
    f.texto_mixto("xpath","admin@yourstore.com","//input[@id='Email']") 
    f.texto_mixto("xpath","admin","//input[contains(@id,'Password')]")
    f.dar_clic_by_xpath("//button[@type='submit'][contains(.,'Log in')]")
    f.tiempo(10)
    
    f.dar_clic_by_xpath("//a[@href='#'][contains(.,'Catalog')]",2)
    f.dar_clic_by_xpath("(//p[contains(.,'Products')])[1]",2)
    f.dar_clic_by_xpath("//a[@href='/Admin/Product/Create']",2)
    
    f.texto_xpath("Leche de Almendras","//input[@id='Name']")
    f.texto_xpath("Esta es una descripcion corta","//textarea[contains(@id,'ShortDescription')]")
    f.dar_clic_by_xpath("//span[@class='tox-mbtn__select-label'][contains(.,'File')]")
    f.dar_clic_by_xpath("//div[@title='New document'][contains(.,'New document')]")
    f.activar_iframe("xpath","/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card[1]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/iframe")
    f.texto_xpath("Esta es una descripcion muy muy muy muy muy my muy muy muy muy larga","//*[@id='tinymce']")
    
    a=f.SEXP("//*[@id='tinymce']")
    a.send_keys(Keys.TAB)
    
    #f.TABULAR(acciones,"NOMBRE")
    #f.controlPlus("a",acciones)
    #acciones.send_ke
    f.tiempo(10)
    
if __name__ == "__main__":
    pytest.main()
    