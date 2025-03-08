"""
Los radio buttons permiten seleccionar solo una opción entre varias.
utilizamos busqueda por XPATH
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.formsite.com/templates/registration-form-templates/")
time.sleep(5)

# Cambiamos al frame donde se encuentra el formulario con los radio buttons
driver.switch_to.frame("iframeResult")

time.sleep(5)

#buscamos el radio button con el valor "male" y lo seleccionamos
male_radio = driver.find_element(By.XPATH, "//input[@value='male']")
male_radio.click()

time.sleep(5)

driver.quit()
