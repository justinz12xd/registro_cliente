# archivo: crear_db.py
import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    cui TEXT NOT NULL,
    departamento TEXT NOT NULL
)
""")

conn.commit()
conn.close()
