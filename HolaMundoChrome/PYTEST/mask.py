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
    
@pytest.mark.notrun   
#se esta diciendo que este test pasando por parametro los datos 
def test9(setup_function,setup2_function):
    f=FuncionesGlobales(d)
    acciones=ActionChains(d)
    print("prueba uno")
    f.tiempo(1)

@pytest.mark.notrun    
#se esta diciendo que este test pasando por parametro los datos 
def test10(setup_function,setup2_function):
    f=FuncionesGlobales(d)
    acciones=ActionChains(d)
    print("prueba uno")
    f.tiempo(1)



#se esta diciendo que este test usa este fixture usando ek @---- arriba del trst
@pytest.mark.notrun
@pytest.mark.usefixtures("setup_function","setup3_function")
def test2():
    f=FuncionesGlobales(d)
    acciones=ActionChains(d)
    print("PRUEBA 2")
    f.tiempo(1)
 
@pytest.mark.run
def test3(): 
    print("demo 2")
    
@pytest.mark.run
def test4(): 
    print("demo 3")
    
@pytest.mark.notrun    
def test5(): 
    print("demo 4")
    
@pytest.mark.run    
def test6(): 
    print("demo 5")    
    
    
@pytest.mark.run    
def test7(): 
    print("demo 5")     

@pytest.mark.notrun    
def test8(): 
    print("demo 1")
         
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