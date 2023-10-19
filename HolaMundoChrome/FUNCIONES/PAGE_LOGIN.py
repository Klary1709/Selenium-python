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


"""
Function -> Function, My_function
Variable -> x, var, myVariable
Class    -> Model, MyClass
Method   -> class_method, method
Constant ->  CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT

"""
T=2

class PageLogin:
    def __init__(self, driver):
        self.driver = driver
        print("PAGE LOGIN ")

         
    def login_master(self,url,user,xpthUser,pas,idPas,xpBtn,tiempo=2):
        d = self.driver
        f = FuncionesGlobales(d)
        f.navegar(url)
        f.texto_xpath(user,xpthUser, T)
        f.texto_id(pas, idPas, T)
        f.dar_clic_by_xpth(xpBtn)
    
    
    def iniciarCiudadano(self,usuario,contra):
        d = self.driver
        f = FuncionesGlobales(d)
        #f.navegar(url)
        f.select_xpath_type("//select[contains(@id,'provider')]","value","11",4)
        f.dar_clic_by_xpath("//button[@type='submit'][contains(.,'Iniciar Sesión')]")
        f.texto_xpath(usuario,"//input[contains(@id,'email')]")
        f.texto_xpath(contra,"//input[contains(@id,'password')]")
        f.dar_clic_by_xpath("//button[@type='submit'][contains(.,'Iniciar Sesión')]")
               
    # def selector_simples(self,ccsSelectorPrin,ccsSelectOpc):
    #     d = self.driver
    #     f = FuncionesGlobales(d)
    #     f.dar_clic_by_ccselector(ccsSelectorPrin)
        

    def selector_simples_ccselector(self, ccselector,texto, tiempo=0 ):
        """
        Este metodo pide el xpath del elemento y le da click
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ccselector)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.CSS_SELECTOR, ccselector)
            valor.click()
            valor.send_keys(texto+Keys.ENTER)
            t=time.sleep(tiempo)
            return t
        
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere clickear con el CCSELECTOR ingresado, posiblemente el xpath este erroneo " 
                  + "\nCCSELECTOR NO ENCONTRADA: " +ccselector
                  )
                

    def selector_simples_xpath(self, xpath,texto, tiempo=0 ):
        """
        Este metodo pide el xpath del elemento y le da click
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor.click()
            valor.send_keys(texto+Keys.ENTER)
            t=time.sleep(tiempo)
            return t
        
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere clickear con el XPATH ingresado, posiblemente el xpath este erroneo " 
                  + "\nXPATH NO ENCONTRADA: " +xpath
                  )



    def selector_simples_name(self, name,texto, tiempo=0 ):
        """
        Este metodo pide el xpath del elemento y le da click
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, name)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.NAME, name)
            valor.click()
            valor.send_keys(texto+Keys.ENTER)
            t=time.sleep(tiempo)
            return t
        
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere clickear con el NAME ingresado, posiblemente el xpath este erroneo " 
                  + "\nNAME NO ENCONTRADA: " + name
                  )

    def selector_simples_id(self, id,texto, tiempo=0 ):
        """
        Este metodo pide el xpath del elemento y le da click
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.ID, id)
            valor.click()
            valor.send_keys(texto+Keys.ENTER)
            t=time.sleep(tiempo)
            return t
        
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere clickear con el ID ingresado, posiblemente el xpath este erroneo " 
                  + "\nID NO ENCONTRADA: " + id
                  )
                   
    def tearDown(self):
        d = self.driver
        d.close()
              
        
        