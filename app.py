from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)

 # Ruta absoluta a la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(basedir, 'db.sqlite3')

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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