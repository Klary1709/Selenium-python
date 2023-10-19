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
    d.get("https://saucelabs.com/") 
    time.sleep(2)
    
    yield
    d.close()
    print("\n    FIN TEST    \n___________________")
 

@pytest.fixture(scope="function")
def setup2_function(): 
    print("ESTO ES DEL SETUP 2 ")
    

@pytest.fixture(scope="function")
def setup3_function(): 
    print("ESTO ES DEL SETUP 3 !!!!!!!!!!!!!!!! ")
    
    
#se esta diciendo que este test pasando por parametro los datos 
def test1(setup_function,setup2_function):
    f=FuncionesGlobales(d)
    acciones=ActionChains(d)
    print("prueba uno")
    f.tiempo(1)

#se esta diciendo que este test usa este fixture usando ek @---- arriba del trst
@pytest.mark.usefixtures("setup_function","setup3_function")
def test2():
    f=FuncionesGlobales(d)
    acciones=ActionChains(d)
    print("PRUEBA 2")
    f.tiempo(1)
    
    
if __name__ == "__main__":
    pytest.main()
    