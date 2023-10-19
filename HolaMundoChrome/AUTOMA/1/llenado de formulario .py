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
CAde=driver.find_element("xpath","//TEXTAREA[@id='currentAddress']/self::TEXTAREA").send_keys("A")
time.sleep(1)

#### sames
#--------------XPATH
PAdd=driver.find_element("xpath","//TEXTAREA[@id='permanentAddress']/self::TEXTAREA").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
PAdd=driver.find_element(By.XPATH,"//TEXTAREA[@id='permanentAddress']/self::TEXTAREA").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
#--------------ID
PAdd=driver.find_element(By.ID,"permanentAddress").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
PAdd=driver.find_element("id","permanentAddress").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
time.sleep(3)
#--------------css
PAdd=driver.find_element(By.CSS_SELECTOR,"#permanentAddress").send_keys("ESTA SI ES")



time.sleep(1)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(3)
driver.find_element("xpath", "//BUTTON[@id='submit']/self::BUTTON").click()


time.sleep(4)
driver.close()