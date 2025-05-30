import re

def validar_login(correo, password):
    if not correo or not password:
        return "Correo y contraseña son obligatorios."
    return "Login válido."

def validar_registro(nombre, email, password1, password2):
    if not nombre or not email or not password1 or not password2:
        return "Todos los campos son obligatorios."
    if password1 != password2:
        return "Las contraseñas no coinciden."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Correo electrónico inválido."
    return "Registro válido."

def validar_cliente(nombre, apellido, cui, departamento):
    if not nombre or not apellido or not cui or not departamento:
        return "Todos los campos del cliente son obligatorios."
    if not cui.isdigit() or len(cui) < 8:
        return "CUI inválido."
    return "Cliente válido."


# # Pruebas de ejemplo
# print(validar_login("usuario@example.com", "12345"))
# print(validar_registro("Juan Pérez", "juan@example.com", "abc123", "abc123"))
# print(validar_cliente("Ana", "Gómez", "12345678", "Guatemala"))
