# ============================================================
# Aqua Tribe Survival - Frontend
# Archivo: app.py
# Descripción: Servidor Flask para la interfaz web del juego
# Proyecto: Aqua Tribe Survival - SENA ADSO
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal (menú del juego)
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta del inventario
@app.route("/inventario")
def inventario():
    return render_template("inventario.html")

# Ruta del mapa
@app.route("/mapa")
def mapa():
    return render_template("mapa.html")
# Ruta de la tribu
@app.route("/tribu")
def tribu():
    return render_template("tribu.html")
if __name__ == "__main__":
    app.run(debug=True)