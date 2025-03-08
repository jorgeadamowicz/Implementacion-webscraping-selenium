from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ruta del archivo local radio_buttons.html
file_path = "file:///D:/Documentos George/Proyectos y practicas/websrapping/selenium/radio_buttons.html"
  

driver = webdriver.Chrome()  # Asegúrate de que ChromeDriver esté configurado
driver.get(file_path)  
time.sleep(5)

# Seleccionar un radio button por su ID
html_radio = driver.find_element(By.ID, "html")
html_radio.click()

time.sleep(5)

# Verificar si está seleccionado
print("¿Está seleccionado?:", html_radio.is_selected())

driver.quit()
