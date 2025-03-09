# Web Scraping con Selenium

## Descripción y referencias a trabajos previos
En este proyecto se pone en práctica el uso de **Selenium** para realizar **web scraping** en sitios web dinámicos. Y es la continuación del trabajo previo, donde realizamos scraping de sitios estáticos. A diferencia de BeautifulSoup, que se usa principalmente para páginas estáticas, Selenium permite interactuar con sitios que cargan contenido de forma asincrónica mediante JavaScript. 
Puedes ver el trabajo previo aquí: [Repositorio de Web Scraping con BeautifulSoup](https://github.com/jorgeadamowicz/implementacion_web_scraping)

En esta práctica se exploró cómo:
- Acceder a elementos web utilizando distintos selectores de Selenium.
- Manejar páginas dinámicas y formularios.
- Extraer datos y manipularlos.
- Aplicar buenas prácticas en la organización del código.

## Tecnologías utilizadas
- **Python**: Lenguaje principal del proyecto.
- **Selenium**: Para la automatización y extracción de datos de páginas dinámicas.
- **PyQt** *(próximamente)*: Para construir una interfaz gráfica que permita interactuar con el scraping de manera más intuitiva.

# Proyecto de Web Scraping con Selenium

Este repositorio contiene ejemplos prácticos de web scraping utilizando Selenium en Python. Además, se exploran conceptos clave relacionados con la automatización de navegadores y el manejo de interfaces web dinámicas.

## Conceptos Claves Aprendidos

- Búsqueda e identificación de elementos en formularios.
- Ubicación de campos utilizando diferentes estrategias de selección:
  - `By.TAG_NAME`
  - `By.ID`
  - `By.CLASS_NAME`
  - `By.NAME`
  - `By.LINK_TEXT`
  - `By.XPATH`
- Completar campos de texto automáticamente.
- Marcar casillas de verificación y botones de opción (`checkboxes` y `radio buttons`).
- Seleccionar opciones en menús desplegables.
- Enviar formularios de manera automatizada.
- Manejo de permisos de acceso y restricciones de seguridad en la web.
- Identificación de mecanismos de protección como **CAPTCHAs**.

## Ejercicios Realizados

- Hacer búsquedas en Google automáticamente.
- Completar formularios de registro en sitios web.
- Iniciar sesión en plataformas con credenciales automatizadas.

## Pendientes a Seguir Trabajando

✅ Agregar selección de múltiples opciones en formularios.
✅ Capturar y procesar mensajes de error o éxito después del envío.
✅ Manejo de alertas y confirmaciones emergentes en páginas web.



## Proyecto en desarrollo
Este proyecto es parte de una serie de prácticas de temas aprendidos durante la cursada de mi *Diplomatura en lenguje Python* y se encuentra en desarrollo. El objetivo es continuar con la práctica, por lo cual este documento se actualizará a medida que avance en la implementación de nuevas funcionalidades y proyectos relacionados con web scraping y automatización de tareas en la web. Actualmente, y como para dar un cierre a esta temática en particular, estoy trabajando en una aplicación para consultar **el clima en tiempo real** mediante web scraping. Para ello, se implementará una interfaz gráfica con **PyQt** para que el usuario pueda ingresar una ciudad y obtener información meteorológica extraída de un sitio web.

