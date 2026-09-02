# ==========================================
# IMPORTACIONES
# ==========================================
from flask import Flask, render_template, request, redirect, url_for

# ==========================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================
app = Flask(__name__)

# ==========================================
# RUTA PRINCIPAL (Formulario)
# ==========================================
@app.route("/")
def index():
    """Muestra el formulario de registro de producto."""
    return render_template("index.html")

# ==========================================
# PROCESAR FORMULARIO (POST Only)
# ==========================================
@app.route("/registrar", methods=["POST"])
def registrar():
    """
    Recibe la información del producto mediante POST,
    la procesa (muestra en consola) y redirige.
    """
    # 1. Obtener los datos usando request.form
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    # 2. Mostrar la información en la terminal con el formato solicitado
    print("\n============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("============================\n")

    # 3. Redireccionar de manera segura usando url_for hacia una ruta GET
    return redirect(url_for("resultado"))

# ==========================================
# MOSTRAR RESULTADO (GET)
# ==========================================
@app.route("/resultado")
def resultado():
    """Muestra la página de éxito tras la redirección."""
    return render_template("resultado.html")

# ==========================================
# SECCIÓN DE AYUDA (Desafío Adicional)
# ==========================================
@app.route("/ayuda")
def ayuda():
    """Explica conceptualmente el comportamiento del protocolo HTTP."""
    return render_template("ayuda.html")

# ==========================================
# EJECUTAR SERVIDOR
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)