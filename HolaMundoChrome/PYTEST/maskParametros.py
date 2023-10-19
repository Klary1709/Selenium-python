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
    d.get("https://www.saucedemo.com/") 
    time.sleep(1)
    
    yield
    d.close()
    print("\n    FIN TEST    \n___________________")

def getData():
    return[
        ("locked_out_user","secret_sauce"),
        ("error_user","secret_sauce"),
        ("problem_user","secret_sauce"),
        ("standard_user","secret_sauce")
    ]
    
#@pytest.mark.usefixtures("setup_function")
@pytest.mark.parametrize("usuario, clave", getData())
def test_login(usuario,clave,setup_function ): 
    f=FuncionesGlobales(d)
    
    f.texto_mixto("XPATH",usuario,"//input[contains(@id,'user-name')]")
    f.texto_mixto("XPATH",clave,"//input[contains(@id,'password')]")
    f.dar_clic_by_xpath("//input[contains(@id,'login-button')]")
    
@pytest.mark.usefixtures("setup_function")
@pytest.mark.parametrize("usuario, clave", getData())
def test_login2 (usuario,clave): 
    f=FuncionesGlobales(d)
    f.texto_mixto("XPATH",usuario,"//input[contains(@id,'user-name')]")
    f.texto_mixto("XPATH",clave,"//input[contains(@id,'password')]")
    f.dar_clic_by_xpath("//input[contains(@id,'login-button')]")
     
    
    
        
    
         
if __name__ == "__main__":
    pytest.main()
    
    
    """
    Se puede compilar de las siguientes formas
    
    ____________________________________________
    pytest Nombre.py -v -s -k "not testAExcluir" 
    pytest mask.py -v -s -k "not cinco" -k "not cuatro"
    se excluye un test cinco y se compila los demas 
    
    pytest Nombre.py -v -s -k "not testAExcluir"
    pytest mask.py -v -s -k cinco -k cuatro 
    solo se compilan los test cinco y cuatro 
    
    ____________________________________________
    si ponemos en     @pytest.mark.DISTIVO
    DISTIVO=es una palabra o nombre para asignar a la mask
    
    pytest Nombre.py -v -s -m DISTINTVO 
    pytest mask.py -v -s -m notrun
    correra todos los que en la maskara tiene el distintivo "notrun" 
    
    
    """