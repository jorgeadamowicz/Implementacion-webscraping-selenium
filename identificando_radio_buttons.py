from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.formsite.com/templates/registration-form-templates/")

# Cambiar al iframe correcto
driver.switch_to.frame("iframeResult")

# Esperar unos segundos para que cargue
time.sleep(5)

# Obtener todos los radio buttons
radio_buttons = driver.find_elements(By.TAG_NAME, "input")

# Imprimir sus atributos
for radio in radio_buttons:
    print(f"Tipo: {radio.get_attribute('type')}, Valor: {radio.get_attribute('value')}")

driver.quit()
