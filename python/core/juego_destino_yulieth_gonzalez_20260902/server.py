from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

# Ruta principal que muestra el formulario para ingresar datos

# Ruta para procesar los datos del formulario y almacenarlos en sesión

# Ruta para mostrar la predicción del futuro basada en los datos ingresados

if __name__ == "__main__":
   app.run(debug=True)