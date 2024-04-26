"""
Prueba de poryecto
V.0.1
"""

# Base de datos de usuarios (simulada)
base_de_datos_usuarios = {
    "usuario1": "contrasenia1",
    "usuario2": "contrasenia2",
    "usuario3": "contrasenia3"
}

def login():
    # Solicitar credenciales al usuario
    usuario = input("Ingrese su nombre de usuario: ")
    contrasenia = input("Ingrese su contraseña: ")

    # Verificar si las credenciales son válidas
    if usuario in base_de_datos_usuarios and base_de_datos_usuarios[usuario] == contrasenia:
        print("Inicio de sesión exitoso. Bienvenido,", usuario)
    else:
        print("Credenciales inválidas. Por favor, inténtelo de nuevo.")

# Ejecutar la función de inicio de sesión
login()