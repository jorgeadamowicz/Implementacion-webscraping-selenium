"""
Ejercicio: Escribir en un campo de búsqueda y enviar

Pasos a seguir:
Abrir Google con Selenium
Ubicar la barra de búsqueda
Escribir un término de búsqueda
Presionar Enter para realizar la búsqueda
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#inicializamos el naegador
driver = webdriver.Chrome()
#abrir google
driver.get('https://www.google.com')

#esperar unos segundos a que la pagina cargue
time.sleep(5)

#busca la barra de busqueda
busqueda = driver.find_element(By.NAME, 'q')

#escribir un término de búsqueda
busqueda.send_keys('automatización con Selenium')

#simular que presionamos 'Enter'
busqueda.send_keys(Keys.RETURN)

#esperar unos segundos a que la pagina cargue los resultados
time.sleep(10)

#cerrar el navegador
driver.quit()