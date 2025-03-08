"""
Ejercicio: Completar un formulario de inicio de sesión

Abrimos la página de inicio de sesión.
Buscamos los campos de usuario y contraseña por su ID (user-name y password).
Escribimos las credenciales de prueba (standard_user y secret_sauce).
Buscamos el botón de login (By.ID, "login-button") y hacemos clic en él con .click().
Esperamos y cerramos el navegador.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#inicializamos el navegador
driver = webdriver.Chrome()
#abrir la página de inicio de sesión
driver.get('https://www.saucedemo.com/')

#esperamos unos segundos a que cargue la pagina
time.sleep(5)

#buscamos los campos usuario y contraseña por su ID
usuario = driver.find_element(By.ID, 'user-name')
contraseña = driver.find_element(By.ID, 'password')

#ingresamos las credenciales de prueba
usuario.send_keys('standard_user')
contraseña.send_keys('secret_sauce')

#buscamos el boton de login y hacemos clic en él
boton = driver.find_element(By.ID, 'login-button')
boton.click()

#esperamos unos segundos a que cargue la pagina
time.sleep(10)

#cerramos el navegador
driver.quit()

