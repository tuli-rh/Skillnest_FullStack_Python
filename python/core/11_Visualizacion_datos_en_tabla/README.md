Objetivo
Desarrollar una aplicación en Flask que permita visualizar una tabla de datos de manera dinámica, enviando información desde el servidor a una plantilla HTML. Se trabajará con la iteración de una lista de diccionarios, el uso de rutas dinámicas, y la aplicación de estilos con CSS o frameworks de diseño para mejorar la presentación de los datos.

¿Por qué es importante?
En el desarrollo web, muchas aplicaciones requieren mostrar datos en forma de tablas dinámicas, como sucede en sistemas de reportes, dashboards o plataformas de gestión. Esta práctica te permitirá comprender cómo:

Enviar datos desde el servidor Flask hacia una plantilla HTML.

Utilizar bucles en Jinja2 para recorrer y renderizar listas de diccionarios.

Aplicar estilos a tablas para mejorar su presentación y usabilidad.

Configurar rutas en Flask para visualizar información de manera estructurada.

Instrucciones
Crea una carpeta llamada tabla_datos_app y dentro de ella, los siguientes ficheros:

Archivo app.py para el servidor Flask.
Carpeta templates/ que contendrá las plantillas HTML.
Archivo templates/tabla.html de la plantilla para mostrar la tabla de datos.
Archivo static/style.css para la hoja de estilos CSS para mejorar la apariencia de la tabla (también puedes utilizar Bootstrap).
Configuración del servidor en el archivo app.py:

from flask import Flask, render_template

app = Flask(**name**)

# Base de datos ficticia de plataformas digitales

datos = [
{"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia"},
{"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
{"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
{"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
{"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
{"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
{"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]

# Ruta para mostrar la tabla con datos

if **name** == "**main**":
app.run(debug=True)
Creación de la plantilla HTML en el archivo tabla.html.

Creación de la hoja de estilos en el archivo style.css

Explicación de las rutas implementadas:

Rutas Descripción Ejemplo de URL Salida esperada
/rutas Muestra la tabla con datos. http://127.0.0.1:5000/tabla Tabla con información de plataformas digitales.
Tips
Flask permite enviar datos a las plantillas HTML con render_template().
Jinja2 en HTML permite utilizar un bucle for para recorrer listas y mostrar información.
Puedes diseñar una experiencia visual más atractiva integrando Bootstrap para mejorar la tabla.
Si la lista de datos está vacía, se muestra un mensaje en lugar de una tabla en blanco.
Contenidos que estás aplicando
Creación de un servidor Flask y configuración de rutas.
Uso de render_template() para enviar información a HTML.
Uso de bucles for en plantillas para recorrer listas de información.
Aplicación de condicionales en Jinja2 ({% if %}) para manejar errores de datos vacíos.
Manejo de archivos estáticos (CSS) en Flask.
Pregunta guía y reflexión
Si quisieras agregar funcionalidades interactivas, como ordenar la tabla por columnas o buscar datos específicos, ¿cómo podrías hacerlo usando JavaScript o filtros en Flask?

Resultado esperado
Al finalizar esta práctica, habrás construido una tabla dinámica en Flask, mostrando información de plataformas digitales de manera organizada y visualmente atractiva.

Ruta: /tabla
