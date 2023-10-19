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
 
 
def test1(setup_function):
    f=FuncionesGlobales(d)
    acciones=ActionChains(d)
    f.navegar("https://saucelabs.com/")
    f.hover_mixto("xpath","//span[@class='MuiTypography-root MuiTypography-buttonLabelNav css-1pj3is7'][contains(.,'Products')]"
                  ,acciones)
    f.hover_mixto("xpath","//span[@class='MuiTypography-root MuiTypography-buttonLabel css-3nj0wx'][contains(.,'Platform for Test')]",
                  acciones)
    
    f.tiempo(10)
    
if __name__ == "__main__":
    pytest.main()
    