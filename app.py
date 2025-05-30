from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, apellido, cui, departamento FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template("index.html", clientes=clientes)

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre = request.form['nombreCliente']
    apellido = request.form['apellidoCliente']
    cui = request.form['cui']
    dep = request.form['dep']

    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, apellido, cui, departamento) VALUES (?, ?, ?, ?)",
                   (nombre, apellido, cui, dep))
    conn.commit()

    cursor.execute("SELECT nombre, apellido, cui, departamento FROM clientes")
    clientes = cursor.fetchall()
    conn.close()

    return jsonify({"success": True, "clientes": clientes})