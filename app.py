# archivo: app.py
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")  # Tu formulario original

@app.route('/clientes')
def ver_clientes():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, apellido, cui, departamento FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template("clientes.html", clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
