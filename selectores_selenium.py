from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#configuramos el webdriver
driver = webdriver.Chrome()
driver.get('https://example.com')

#obtenemos el titulo de la pagina utilizando selenuim
titulo = driver.find_element(By.TAG_NAME,'h1') #busca la etiquet "h1"
print(f"el tiutlo de la pagina es: {titulo.text}") # muestra el resultado

#buscamos un elemento por clase CSS
# objeto_clase = driver.find_element(By.CLASS_NAME, "Example") #busca la clase 'example'
# print(f"el objeto de la clase es: {objeto_clase.text}") #muestra el resultado

#mantener la ventana abierta hasta que el usario presione 'enter'
input("Presiona 'Enter' para cerrar la ventana del navegador")
driver.quit() #cierra la ventana del navegador

"""
Ejemplo de métodos de búsqueda con By:

driver.find_element(By.TAG_NAME, "h1")  # Encuentra por etiqueta <h1>
driver.find_element(By.ID, "mi_id")  # Encuentra por ID
driver.find_element(By.CLASS_NAME, "mi_clase")  # Encuentra por clase CSS
driver.find_element(By.NAME, "mi_nombre")  # Encuentra por atributo "name"
driver.find_element(By.LINK_TEXT, "Texto del enlace")  # Encuentra enlaces
"""


