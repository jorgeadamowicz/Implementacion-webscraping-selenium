from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

time.sleep(5)

#buacmos los checkboxes
checkboxes = driver.find_elements(By.TAG_NAME, 'input')

#marcamos el primer checkbox si no esta marcado
if not checkboxes[0].is_selected():
    checkboxes[0].click()
    
#desmarcamos el segundo checkbox si esta marcado
if checkboxes[1].is_selected():
    checkboxes[1].click()
    
time.sleep(10)

driver.quit()

