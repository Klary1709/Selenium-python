import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Crear un objeto de WebDriver
driver = selenium.webdriver.Chrome()

# Abrir la página web
driver.get("https://dtc.ventanilla.simple.sv/etapas/ejecutar/2967049")

# Seleccionar la opción "Nombre del trámite"
element = driver.find_element_by_id("nombre_tramite")
element.click()

# Ingresar el nombre del trámite
element.send_keys("Trámite de prueba")

# Seleccionar la opción "Tipo de trámite"
element = driver.find_element_by_id("tipo_tramite")
element.click()

# Ingresar el tipo de trámite
element.send_keys("Trámite de prueba")

# Seleccionar la opción "Número de tramite"
element = driver.find_element_by_id("numero_tramite")
element.click()

# Ingresar el número de tramite
element.send_keys("123456")

# Seleccionar la opción "Departamento"
element = driver.find_element_by_id("departamento")
element.click()

# Ingresar el departamento
element.send_keys("San Salvador")

# Seleccionar la opción "Municipio"
element = driver.find_element_by_id("municipio")
element.click()

# Ingresar el municipio
element.send_keys("San Salvador")

# Seleccionar la opción "Dirección"
element = driver.find_element_by_id("direccion")
element.click()

# Ingresar la dirección
element.send_keys("Calle 10a Poniente, San Salvador")

# Seleccionar la opción "Teléfono"
element = driver.find_element_by_id("telefono")
element.click()

# Ingresar el teléfono
element.send_keys("2222-2222")

# Seleccionar la opción "Correo electrónico"
element = driver.find_element_by_id("correo_electronico")
element.click()

# Ingresar el correo electrónico
element.send_keys("test@example.com")

# Seleccionar la opción "Observaciones"
element = driver.find_element_by_id("observaciones")
element.click()

# Ingresar las observaciones
element.send_keys("Observaciones de prueba")

# Hacer clic en el botón "Enviar"
element = driver.find_element_by_id("enviar")
element.click()

# Comprobar que el mensaje de confirmación es correcto
message = driver.find_element_by_id("mensaje").text
if message == "Trámite enviado correctamente":
    print("El trámite se envió correctamente")
else:
    print("El trámite no se envió correctamente")

# Cerrar el navegador web
driver.quit()