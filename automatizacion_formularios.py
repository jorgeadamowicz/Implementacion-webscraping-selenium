"""
Automatización de formularios completos usando Selenium. 
En este ejercicio aprenderemos a:

Completar campos de texto
Identificar elementos del formulario: ubicando los campos con ID, name, class, XPath, etc.
Seleccionar opciones en menús desplegables
Marcar casillas de verificación y botones de opción (checkboxes y radio buttons)
Enviar el formulario

Objetivos:
✅ Completar campos de texto
✅ Seleccionar opciones de radio y checkboxes
✅ Elegir una fecha
✅ Seleccionar un valor en un menú desplegable
✅ Enviar el formulario

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#opciones del navegador
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-blink-features=AutomationControlled")

#iniciar el navegaror
driver = webdriver.Chrome(options=options)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

# Esperar hasta que el formulario cargue
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "firstname")))

#completar el formulario
driver.find_element(By.NAME, "firstname").send_keys("George")
driver.find_element(By.NAME, "lastname").send_keys("Maquinola")

#seleccionar genero (radio button)
driver.find_element(By.XPATH, "//input[@name='sex' and @value='Male']").click()

#seleccionar experiencia (radio button)
driver.find_element(By.XPATH, "//input[@name='exp' and @value='3']").click()

#insertar fecha (datapicker)
driver.find_element(By.ID, "datepicker").send_keys("01/03/2025")

#seleccionar profesion (checkbox)
checkbox = driver.find_element(By.XPATH, "//input[@name='profession' and @value='Automation Tester']")
# Desplazar la página hasta el elemento
driver.execute_script("arguments[0].scrollIntoView();", checkbox)
checkbox.click()

#seleccionar continente (dropdown)
continents_dropdown = Select(driver.find_element(By.ID, "continents"))
continents_dropdown.select_by_visible_text("South America")

#enviar el formulario
driver.find_element(By.ID, "submit").click()

time.sleep(10)
driver.quit()