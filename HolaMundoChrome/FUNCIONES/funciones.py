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
from selenium.webdriver import ActionChains

import sys

"""
Function -> Function, My_function
Variable -> x, var, myVariable
Class    -> Model, MyClass
Method   -> class_method, method
Constant ->  CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT
"""


class FuncionesGlobales:
    global acciones 
    def __init__(self, driver):
        self.driver = driver
        #print("Estamos en funciones globalees")
        
    def tiempo(self, tie):
        t = time.sleep(tie)
        return t
        
    def navegar(self, Url, tiempo=0):
        """
        Este metodo redirecciona a el sitio web y se le puede dar un tiempo de espera en pantalla a la acción
        """
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Pagina abierta: "+str(Url))
        t = time.sleep(tiempo)
        return t


    def login(self, nom, xpahnom, pas, xpathpas, xpathBtn, tiempo=0):
        """
        Este metodo pide los parámetros de xpath y el valor del sendkeys para los campos de
        usuario y contraseña y el xpath del botón de iniciar
        por defecto tiene un tiempo de 0 segundos, y este puede ser modificado
        """

        nombre = self.driver.find_element(By.XPATH, xpahnom)
        nombre.send_keys(nom)
        t = time.sleep(tiempo)
        contra = self.driver.find_element(By.XPATH, xpathpas)
        contra.send_keys(pas)
        t = time.sleep(tiempo)
        btnSing = self.driver.find_element(By.XPATH, xpathBtn)
        btnSing.click()
        t = time.sleep(tiempo)
        return t

#ingresar datos
    def texto_xpath(self, texto, xpath, tiempo=0):
        """
        Este metodo permite localizar un elemento con el xpath y setear la información
        de forma opcional asignar un tiempo para esta acción
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))#si existe el elementp
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)#busca el elemento en toda la pagina
            valor = self.driver.find_element(By.XPATH, xpath) #crea el objeto del elemento segun su xpath 
            valor.clear()  # limpia el campo por si ya tiene un valor asi no lo concatena
            valor.send_keys(texto)
            print("Escribiendo en el campo {} el texto ->> {}".format(xpath,texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento con el XPATH que se ha ingresado para el campo"+ texto 
                  + "\nXPATH NO ENCONTRADA: " +xpath 
                  )

    def texto_id(self, texto, id, tiempo=0):
        """
        Este metodo permite localizar un elemento con el id y setear la información
        de forma opcional asignar un tiempo para esta acción
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id))) #si existe para el except
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor) #busca el elemento en toda la pag
            valor = self.driver.find_element(By.ID, id) #crea el elemento indicando el id
            valor.clear()  # limpia el campo por si ya tiene un valor asi no lo concatena
            valor.send_keys(texto)
            print("Escribiendo en el campo {} el texto ->> {}".format(id,texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento con el ID que se ha ingresado para el campo "+ texto 
                  + "\nID NO ENCONTRADO: " +id
                  )

    def texto_mixto(self, tipo,texto, elemento, tiempo=0): 
        """
        Este metodo permite localizar un elemento con el xpath y setear la información
        de forma opcional asignar un tiempo para esta acción

            tipo: xpath ó id
            texto: el texto a ingresar en el campo
            elemento: el identificador único de cada elemento que debe ser correspondiente al tipo seleccionado
        """         
        tipo=str(tipo)
        
        
        if(tipo.lower()=="xpath"): 
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))#si existe el elementp
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)#busca el elemento en toda la pagina
                valor = self.driver.find_element(By.XPATH, elemento) #crea el objeto del elemento segun su xpath 
                valor.clear()  # limpia el campo por si ya tiene un valor asi no lo concatena
                valor.send_keys(texto)
                print("Escribiendo en el campo {} el texto ->> {}".format(elemento,texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento con el XPATH que se ha ingresado para el campo"+ texto 
                    + "\nXPATH NO ENCONTRADA: " +elemento  
                    )            
        elif(tipo.lower()=="id"):
            """
            Este metodo permite localizar un elemento con el id y setear la información
            de forma opcional asignar un tiempo para esta acción
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento))) #si existe para el except
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor) #busca el elemento en toda la pag
                valor = self.driver.find_element(By.ID, elemento) #crea el elemento indicando el id
                valor.clear()  # limpia el campo por si ya tiene un valor asi no lo concatena
                valor.send_keys(texto)
                print("Escribiendo en el campo {} el texto ->> {}".format(elemento,texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento con el ID que se ha ingresado para el campo "+ texto 
                    + "\nID NO ENCONTRADO: " +elemento 
                    )            
        

# FUNCIONES PARA BUSCAR, ENCONTRAR Y ALAMACENAR UN ELEMENTO EN UNA VARIABLE WEBDRIVERWAIT
    def SEXP(self, elemento):
        """FUNCION PARA BUSCAR,ENCONTRAR Y ALAMACENAR UN ELEMENTO PARA PODER ACCEDER A LAS FUNCIONES DE UN COMPONENTE WEBDRIVERWAIT UN ELEMENTO POR XPATH

        Args:
            elemento (XPATH): el xpath del elemento 

        Returns:
            valor: una variable tipo WebDriverWait para acceder a las funciones de ese elemento 
        """
        valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
        valor = self.driver.find_element(By.XPATH, elemento)
        return valor   
    
    def SEID(self, elemento):
        """FUNCION PARA BUSCAR,ENCONTRAR Y ALAMACENAR UN ELEMENTO PARA PODER ACCEDER A LAS FUNCIONES DE UN COMPONENTE WEBDRIVERWAIT UN ELEMENTO POR ID

        Args:
            elemento (ID): el ID del elemento 

        Returns:
            valor: una variable tipo WebDriverWait para acceder a las funciones de ese elemento 
        """
        valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
        valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
        valor = self.driver.find_element(By.ID, elemento)
        return valor 
       
    def SECSS(self, elemento):
        """FUNCION PARA BUSCAR,ENCONTRAR Y ALAMACENAR UN ELEMENTO PARA PODER ACCEDER A LAS FUNCIONES DE UN COMPONENTE WEBDRIVERWAIT UN ELEMENTO POR CSSSELECTOR

        Args:
            elemento (CSSSELECTOR): el CSSSELECTOR del elemento 

        Returns:
            valor: una variable tipo WebDriverWait para acceder a las funciones de ese elemento 
        """
        valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
        valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
        valor = self.driver.find_element(By.CSS_SELECTOR, elemento)
        return valor 
    

#Clickear elementos
    
    def dar_clic_by_xpath(self, xpathbtn, tiempo=0 ):
        """
        Este metodo pide el xpath del elemento y le da click
        """
        try:
            valor=self.SEXP(xpathbtn)
            valor.click()
            print("Damos clic en el campo->> "+xpathbtn)
            t=time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere clickear con el XPATH ingresado, posiblemente el xpath este erroneo " 
                  + "\nXPATH NO ENCONTRADA: " +xpathbtn
                  )

    def dar_clic_by_id(self, idBtn, tiempo=0 ):
        """
        Este metodo pide el id del elemento y le da click
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, idBtn)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.ID, idBtn)
            valor.click()
            print("Damos clic en el campo->> "+idBtn)
            t=time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere clickear con el ID ingresado, posiblemente el xpath este erroneo " 
                  + "\nID NO ENCONTRADO: " +idBtn
                  )

    def dar_clic_by_ccselector(self, ccselector, tiempo=0 ):
        """
        Este metodo pide el xpath del elemento y le da click
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ccselector)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.CSS_SELECTOR, ccselector)
            valor.click()
            print("Damos clic en el campo->> "+ccselector)
            t=time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere clickear con el CCSELECTOR ingresado, posiblemente el CSS_SELECTOR este erroneo " 
                  + "\nCCSELECTOR NO ENCONTRADA: " +ccselector
                  )

    def clic_mixto(self,tipo,elemento, tiempo=0): 
        """
        Este metodo permite clickear un elemento especificando su tipo de indicador y indicador unico
            tipo: xpath,id,css
            elemento: el identificador único del elemento 
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.XPATH, elemento)
                valor.click()
                print("Damos clic en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere clickear con el XPATH ingresado, posiblemente el xpath este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " +elemento
                    )
        elif(tipo.lower()=="id"):
            """
            Este metodo pide el id del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.ID, elemento)
                valor.click()
                print("Damos clic en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere clickear con el ID ingresado, posiblemente el xpath este erroneo " 
                    + "\nID NO ENCONTRADO: " +elemento
                    )       
        elif(tipo.lower()=="css"):
            """
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.CSS_SELECTOR, elemento)
                valor.click()
                print("Damos clic en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere clickear con el CCSELECTOR ingresado, posiblemente el CSS_SELECTOR este erroneo " 
                    + "\nCCSELECTOR NO ENCONTRADA: " +elemento
                    )
    
    
    #FUNCIONES DEL MOUSE
    def clicdoble_mixto(self,tipo,elemento, tiempo=0): 
        """
        Este metodo permite clickear un elemento especificando su tipo de indicador y indicador unico
            tipo: xpath,id,css
            elemento: el identificador único del elemento 
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        accion = ActionChains(self.driver)
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor=self.SEXP(elemento)
                accion.double_click(valor).perform()
                print("Damos doble clic en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere clickear con el XPATH ingresado, posiblemente el xpath este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " +elemento
                    )
        elif(tipo.lower()=="id"):
            """
            Este metodo pide el id del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.ID, elemento)
                accion.double_click(valor).perform()
                print("Damos doble clic en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere clickear con el ID ingresado, posiblemente el xpath este erroneo " 
                    + "\nID NO ENCONTRADO: " +elemento
                    )       
        elif(tipo.lower()=="css"):
            """
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.CSS_SELECTOR, elemento)
                accion.double_click(valor).perform()
                print("Damos doble clic en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere clickear con el CCSELECTOR ingresado, posiblemente el CSS_SELECTOR este erroneo " 
                    + "\nCCSELECTOR NO ENCONTRADA: " +elemento
                    )
    
    def clic_derecho_mixto(self,tipo,elemento, tiempo=0): 
        """
        Este metodo permite dar clic derecho un elemento especificando su tipo de indicador y indicador unico
            tipo: xpath,id,css
            elemento: el identificador único del elemento 
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        accion = ActionChains(self.driver)
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor=self.SEXP(elemento)
                accion.context_click(valor).perform()
                print("Damos clic derecho en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere dar clic derecho con el XPATH ingresado, posiblemente el xpath este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " +elemento
                    )
        elif(tipo.lower()=="id"):
            """
            Este metodo pide el id del elemento y le da click
            """
            try:
                valor=self.SEID(elemento)
                accion.context_click(valor).perform()
                print("Damos clic derecho en el campo->> "+elemento)
                
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere dar clic derecho con el ID ingresado, posiblemente el xpath este erroneo " 
                    + "\nID NO ENCONTRADO: " +elemento
                    )       
        elif(tipo.lower()=="css"):
            """
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor=self.SECSS(elemento)
                accion.context_click(valor).perform()
                print("Damos clic derecho en el campo->> "+elemento)
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere dar clic derecho con el CCSELECTOR ingresado, posiblemente el CSS_SELECTOR este erroneo " 
                    + "\nCCSELECTOR NO ENCONTRADA: " +elemento
                    )

   
    def clic_y_arrastrar(self,tipo,elemento,destino, tiempo=0): 
        """
        Este metodo permite dar clic a un elemento especificando su tipo de indicador y indicador unico, y arrastrarlo a otro elemento destino 
            tipo: xpath,id,css
            elemento: el identificador único del elemento 
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        accion = ActionChains(self.driver)
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click y lo arrastra a un destino
            """
            try:
                valor=self.SEXP(elemento)
                try: 
                    valor=self.SEXP(destino)
                    valordestino=self.SEXP(destino)
                    accion.drag_and_drop(valor,valordestino).perform()
                    print("Damos clic en el campo->> "+elemento+ " y se arrastro al campo " + destino)
                    t=time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print("\nNo se ha encontrado el elemento destino con el XPATH ingresado, posiblemente el xpath este erroneo " 
                        + "\nXPATH NO ENCONTRADA: " +destino
                        )
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere arrastrar con el XPATH ingresado, posiblemente el xpath este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " +elemento
                    )
        elif(tipo.lower()=="id"):
            """ 
            Este metodo pide el ID del los elementos y le da click y lo arrastra a un destino
            """
            try:
                valor=self.SEID(elemento)
                try: 
                    valordestino=self.SEID(destino)
                    accion.drag_and_drop(valor,valordestino).perform()
                    print("Damos clic en el campo->> "+elemento+ " y se arrastro al campo " + destino)
                    t=time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print("\nNo se ha encontrado el elemento destino con el ID ingresado, posiblemente el xpath este erroneo " 
                        + "\ID NO ENCONTRADA: " +destino
                        )
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere arrastrar con el ID ingresado, posiblemente el ID este erroneo " 
                    + "\ID NO ENCONTRADA: " +elemento
                    )    
        elif(tipo.lower()=="css"):
            """ 
            Este metodo pide el CSS del los elementos y le da click y lo arrastra a un destino
            """
            try:
                valor=self.SECSS(elemento)
                try: 
                    valordestino=self.SECSS(destino)
                    accion.drag_and_drop(valor,valordestino).perform()
                    print("Damos clic en el campo->> "+elemento+ " y se arrastro al campo " + destino)
                    t=time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print("\nNo se ha encontrado el elemento destino con el CSS ingresado, posiblemente el CSS este erroneo " 
                        + "\CSS NO ENCONTRADA: " +destino
                        )
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere arrastrar con el CSS ingresado, posiblemente el CSS este erroneo " 
                    + "\CSS NO ENCONTRADA: " +elemento
                    )   

   
    def clic_y_arrastrarXY(self,tipo,frame,elemento,X,Y, tiempo=0): 
        """
        Este metodo permite dar clic a un elemento especificando su tipo de indicador y indicador unico, y arrastrarlo dentro de un iframe 
            tipo: xpath,id,css
            frame: el identificador único del frame 
            elemento: el identificador único del elemento 
            X: Posicion horizontal 
            Y: Posicion vertical
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        accion = ActionChains(self.driver)
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click y lo arrastra dentro de un  iframe
            """
            try:
                valorFrame=self.SEXP(frame)
                try:
                    fr=self.driver.find_element(By.XPATH,frame)
                    self.driver.switch_to.frame(fr)
                    valor=self.SEXP(elemento)
                    accion.drag_and_drop_by_offset(valor,X,Y).perform()
                    print("Damos clic en el campo->> {}\n     se arrastro dentro del frame-> {} \n     en las coordenadas ( {},{})\n".format(elemento,frame,X,Y))
                    t=time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print("\nNo se ha encontrado el elemento que se quiere arrastrar con el XPATH ingresado, posiblemente el xpath este erroneo " 
                            + "\nXPATH NO ENCONTRADA: " +elemento
                        )
            except TimeoutException as ex:
                print("\nNo se ha encontrado el frame con el XPATH ingresado, posiblemente el xpath este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " +frame
                    )
        elif(tipo.lower()=="id"):
            """ 
            Este metodo pide el ID del elemento y le da click y lo arrastra dentro de un iframe
            """
            try:
                valorFrame=self.SEID(frame)
                try:
                    fr=self.driver.find_element(By.ID,frame)
                    self.driver.switch_to.frame(fr)
                    valor=self.SEID(elemento)
                    accion.drag_and_drop_by_offset(valor,X,Y).perform()
                    print("Damos clic en el campo->> {}\n     se arrastro dentro del frame-> {} \n     en las coordenadas ( {},{})\n".format(elemento,frame,X,Y))
                    t=time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print("\nNo se ha encontrado el elemento que se quiere arrastrar con el ID ingresado, posiblemente el xpath este erroneo " 
                            + "\nXPATH NO ENCONTRADA: " +elemento
                        )
            except TimeoutException as ex:
                print("\nNo se ha encontrado el frame con el ID ingresado, posiblemente el xpath este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " +frame
                    )  
        elif(tipo.lower()=="css"):
            """ 
            Este metodo pide el CSS del los elementos y le da click y lo arrastra a un destino
            """
            try:
                valorFrame=self.SECSS(frame)
                try:
                    fr=self.driver.find_element(By.CSS_SELECTOR,frame)
                    self.driver.switch_to.frame(fr)
                    valor=self.SECSS(elemento)
                    accion.drag_and_drop_by_offset(valor,X,Y).perform()
                    print("Damos clic en el campo->> {}\n     se arrastro dentro del frame-> {} \n     en las coordenadas ( {},{})\n".format(elemento,frame,X,Y))
                    t=time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print("\nNo se ha encontrado el elemento que se quiere arrastrar con el CSS ingresado, posiblemente el xpath este erroneo " 
                            + "\nXPATH NO ENCONTRADA: " +elemento
                        )
            except TimeoutException as ex:
                print("\nNo se ha encontrado el frame con el CSS ingresado, posiblemente el xpath este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " +frame
                    )  

   
    def clicXY(self,tipo,elemento,X,Y, tiempo=0): 
        """
        Este metodo permite dar clic a un elemento especificando su tipo de indicador y indicador unico, y arrastrarlo dentro de un iframe 
            tipo: xpath,id,css
            frame: el identificador único del frame 
            elemento: el identificador único del elemento 
            X: Posicion horizontal 
            Y: Posicion vertical
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        accion = ActionChains(self.driver)
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click y lo arrastra dentro de un  iframe
            """
            try:
                #fr=self.driver.find_element(By.XPATH,frame)
                #self.driver.switch_to.frame(fr)
                valor=self.SEXP(elemento)
                accion.move_to_element_with_offset(valor,X,Y).click().perform()
                print("\nDamos clic en el campo->> {}, con coordenadas {} , {}".format(elemento,X,Y))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere arrastrar con el XPATH ingresado, posiblemente el xpath este erroneo " 
                        + "\nXPATH NO ENCONTRADA: " +elemento
                    )

        elif(tipo.lower()=="id"):
            """ 
            Este metodo pide el ID del elemento y le da click y lo arrastra dentro de un iframe
            """

            try:
                valor=self.SEID(elemento)
                accion.move_to_element_with_offset(valor,X,Y).click().perform()
                print("\nDamos clic en el campo->> {}, con coordenadas {} , {}".format(elemento,X,Y))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere arrastrar con el ID ingresado, posiblemente el xpath este erroneo " 
                        + "\nID NO ENCONTRADO: " +elemento
                    )

        elif(tipo.lower()=="css"):
            """ 
            Este metodo pide el CSS del los elementos y le da click y lo arrastra a un destino
            """
            try:
                valor=self.SECSS(elemento)
                accion.move_to_element_with_offset(valor,X,Y).click().perform()
                print("\nDamos clic en el campo->> {}, con coordenadas {} , {}".format(elemento,X,Y))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere arrastrar con el CSS ingresado, posiblemente el xpath este erroneo " 
                        + "\nXPATH NO ENCONTRADA: " +elemento
                    )



#funciones para elementos de selección multiple
    def select_xpath_type(self, xpath, tipo, dato, tiempo=0 ):
        """
        Este metodo selecciona buscando el elemento según el XPATH, especificando el tipo de inidicador dentro del select y el valor a buscar 
            xpath(str): indicador unico por xpath
            tipo (str): text,index,value  
            dato (str): el dato a buscar ya sea texto visible, numero de indice o el "value"}
            tiempo(int): tiempo por defecto 0
        """
        
        tipo=str(tipo)
        tipo.lower()        
        try: # si existe 
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor=Select(valor)            
            if(tipo=="text"):
                valor.select_by_visible_text(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            elif(tipo=="index"):
                valor.select_by_index(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            elif(tipo=="value"):
                valor.select_by_value(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            t=time.sleep(tiempo)
            return t
        except TimeoutException as ex: # si no existe 
            print("\nNo se ha encontrado el elemento que se quiere seleccionar con el XPATH ingresado, posiblemente el xpath este erroneo " 
                  + "\nXPATH NO ENCONTRADA: " +xpath
                  )

    def select_id_type(self, id, tipo, dato, tiempo=0 ):
        """
        Este metodo selecciona buscando el elemento según el ID, especificando el tipo de inidicador dentro del select y el valor a buscar 
            id: indicador unico por ID
            tipo: text,index,value  
            dato: el dato a buscar ya sea texto visible, numero de indice o el "value"
        """
        tipo=str(tipo)
        
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.ID, id)
            
            valor=Select(valor)            
            if(tipo.lower()=="text"):
                valor.select_by_visible_text(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            
            elif(tipo.lower()=="index"):
                valor.select_by_index(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            
            elif(tipo.lower()=="value"):
                valor.select_by_value(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            
            t=time.sleep(tiempo)
            return t
        
        
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere seleccionar con el ID ingresado, posiblemente el ID este erroneo " 
                  + "\nID NO ENCONTRADA: " +id
                  )

    def select_ccsselector_type(self, css, tipo, dato, tiempo=0 ):
        """
        Este metodo selecciona buscando el elemento según el ccsselector, especificando el tipo de inidicador dentro del select y el valor a buscar 
            ccsselector: indicador unico por ccsselector
            tipo: text,index,value  
            dato: el dato a buscar ya sea texto visible, numero de indice o el "value"
        """
        tipo=str(tipo)
        
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.CSS_SELECTOR, css)
            valor=Select(valor)            
            if(tipo.lower()=="text"):
                valor.select_by_visible_text(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            elif(tipo.lower()=="index"):
                valor.select_by_index(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            elif(tipo.lower()=="value"):
                valor.select_by_value(dato)
                print("El campo seleccionado ->> "+dato +" segun "+tipo)
            t=time.sleep(tiempo)
            return t
        
        
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere seleccionar con el CSS_SELECTOR ingresado, posiblemente el CSS_SELECTOR este erroneo " 
                  + "\nCSS_SELECTOR NO ENCONTRADA: " +css
                  )

#Funciones para cargar archivos 
    def subirarch_xpath(self, ruta ="C://agregarLaDoblefleca", xpath="" ,  tiempo=0 ):
        """
        NOTA:  SE DEBE AGREGAR LA DOBLE // EN EN LA URL     
        Este metodo selecciona buscando el elemento según el XPATH y sube un archivo
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor.send_keys(ruta)    
            print("Se cargo el archivo ->> "+ruta)
            t=time.sleep(tiempo)
            return t
         
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere seleccionar con el XPATH ingresado, posiblemente el XPATH este erroneo " 
                  + "\nXPATH NO ENCONTRADA: " +xpath
                  )

    def subirarch_id(self, ruta ="C://agregarLaDoblefleca" ,id="id",  tiempo=0 ):
        """
        NOTA:  SE DEBE AGREGAR LA DOBLE // EN EN LA URL     
        Este metodo selecciona buscando el elemento según el ID y sube un archivo
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.ID, id)
            valor.send_keys(ruta)    
            print("Se cargo el archivo ->> "+ruta)
            t=time.sleep(tiempo)
            return t
         
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere seleccionar con el ID ingresado, posiblemente el ID este erroneo " 
                  + "\nID NO ENCONTRADA: " +id
                  )

    def subirarch_csselector(self, ruta ="C://agregarLaDoblefleca" ,css="cssSelector" ,  tiempo=0 ):
        """
        NOTA:  SE DEBE AGREGAR LA DOBLE // EN EN LA URL     
        Este metodo selecciona buscando el elemento según el CSS SELECTOR y sube un archivo
        """
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))
            valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.CSS_SELECTOR, css)
            valor.send_keys(ruta)    
            print("Se cargo el archivo ->> "+ruta)
            t=time.sleep(tiempo)
            return t
         
        except TimeoutException as ex:
            print("\nNo se ha encontrado el elemento que se quiere seleccionar con el CSS_SELECTOR ingresado, posiblemente el CSS_SELECTOR este erroneo " 
                  + "\nCSS_SELECTOR NO ENCONTRADA: " + css
                  )


#Funcion para checkes multiples 
    def checkmultiple_xpath(self,*args,tiempo=0 ):
        """    
        Este metodo selecciona buscando el elemento según el XPATH y sube un arc
        """
        
        for num in args:
            try:
                    valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, num)))
                    valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                    valor = self.driver.find_element(By.XPATH, num)
                    valor.click()  
                    print("click en el elemento ->> "+num)
                    
            
            except TimeoutException as ex:
                print("\nNo se ha encontrado el elemento que se quiere seleccionar con el XPATH ingresado, posiblemente el XPATH este erroneo " 
                    + "\nXPATH NO ENCONTRADA: " + num
                    )
        t=time.sleep(tiempo)
        return t

#COMANDOS BASICOS
    def controlPlus(self,letra,acciones,tiempo=0):
        """Esta funcion simula la accion de presionr control +  un letra y soltar control 

        Args:
            letra (str): la letra que quiere usar en el comando 
            acciones (ActionChains): una variable ActionChains inicializada en el test
            tiempo (int, optional): _description_. Defaults to 0.
            
        ejemplo de aplicacion:
            acciones=ActionChains(d)
            // f.controlPlus("a",acciones)
        """
        #acciones=ActionChains(self.driver)
        acciones.key_down(Keys.CONTROL).send_keys(letra).key_up(Keys.CONTROL).perform()
        tiempo=time.sleep(tiempo)
        print("Se ejecuto el comando CTRL+{}".format(letra))
        return tiempo

        
    def TABULAR(self, acciones, tiempo=0):
        """Esta funcion simula la accion de presionr la tecla tabulador  pasando como parametro una variable tipo ActionChains
        

        Args:
            acciones (ActionChains): esta variable debe ser tipo ActionChain
            tiempo (int es optional): Defaults to 0.
            
        ejemplo de aplicacion: 
            acciones=ActionChains(d)
            // f.TABULAR(acciones)
        """
        #acciones=ActionChains(self.driver)
        acciones.send_keys(Keys.TAB)
        tiempo=time.sleep(tiempo)
        print("Se presiono la tecla TAB ")
        return tiempo
        
        

#EXTRAS
    def salida():
        print("Prueba Finalizada")
 
 
    def existe(self,tipo,elemento, tiempo=0): 
        """
        Esta funcion retona el  strinf "existe" y "no existe"
        Este metodo permite clickear un elemento especificando su tipo de indicador y indicador unico
            tipo: xpath,id,css
            elemento: el identificador único del elemento segun el tipo seleccionado
            tiempo: tiempo de retraso 
        """
        tipo=str(tipo)
        
        if(tipo.lower()=="xpath"):
            """ 
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.XPATH, elemento)
                print("El elemento: "+elemento+" existe")
                t=time.sleep(tiempo)
                return "existe" 
            except TimeoutException as ex:
                print("El elemento: "+elemento+" NO existe")
                return "no existe"
        elif(tipo.lower()=="id"):
            """
            Este metodo pide el id del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.ID, elemento)
                print("El elemento: "+elemento+" existe")
                t=time.sleep(tiempo)
                return "existe" 
            except TimeoutException as ex:
                print("El elemento: "+elemento+" NO existe")
                return "no existe"
        elif(tipo.lower()=="css"):
            """
            Este metodo pide el xpath del elemento y le da click
            """
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
                valor=self.driver.execute_script("arguments[0].scrollIntoView();",valor)
                valor = self.driver.find_element(By.CSS_SELECTOR, elemento)
                print("El elemento: "+elemento+" existe")
                t=time.sleep(tiempo)
                return "existe" 
            except TimeoutException as ex:
                print("El elemento: "+elemento+" NO existe")
                return "no existe"


    def tearDown(self): 
        d = self.driver
        d.close()
        

# > python -m PRACTCA2.Practica1uni
