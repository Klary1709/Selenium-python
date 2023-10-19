import time
from xml.etree.ElementPath import xpath_tokenizer

from selenium import webdriver
from  selenium.webdriver.common.by import By

driver=webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)


nombre=driver.find_element("xpath","//INPUT[@id='userName']/self::INPUT")
nombre.send_keys("Marina")
time.sleep(1)
email=driver.find_element("xpath","//INPUT[@id='userEmail']/self::INPUT")
email.send_keys("Marina@yopmail.com")
time.sleep(1)

'''
DOSsameTimeA=driver.find_elements(By.TAG_NAME,"textarea")
time.sleep(3)
'''
DOSsameTime2=driver.find_element(By.TAG_NAME,"textarea") and driver.find_element(By.CSS_SELECTOR,"#permanentAddress").send_keys(" PERO ESTE SE AGREGA AQUI ")

CAde=driver.find_element("xpath","//TEXTAREA[@id='currentAddress']/self::TEXTAREA").send_keys("A")
time.sleep(1)

#### sames
#--------------XPATH
PAdd=driver.find_element("xpath","//TEXTAREA[@id='permanentAddress']/self::TEXTAREA").send_keys("A")

PAdd=driver.find_element("xpath","//TEXTAREA[@id='permanentAddress']/self::TEXTAREA").clear()
time.sleep(2)
PAdd=driver.find_element(By.XPATH,"//TEXTAREA[@id='permanentAddress']/self::TEXTAREA").send_keys("B")
#--------------ID
PAdd=driver.find_element(By.ID,"permanentAddress").send_keys("C")
PAdd=driver.find_element("id","permanentAddress").send_keys("D")
time.sleep(3)
#--------------css
PAdd=driver.find_element(By.CSS_SELECTOR,"#permanentAddress") and driver.find_element(By.ID,"permanentAddress").send_keys("SE AGREGARA?")



time.sleep(1)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(3)
driver.find_element("xpath", "//BUTTON[@id='submit']/self::BUTTON").click()


time.sleep(4)
driver.close()