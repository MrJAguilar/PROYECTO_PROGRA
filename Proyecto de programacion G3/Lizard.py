
"""
Proyecto de programación

Estudiantes encargados:
Jefferson Aguilar Mendoza
Juan Pablo Vergara Cholele
Jonatan Pereira Guevara
Geovanna Castro Sanchez

Universidad Fidelitas
"""

# Base de datos de usuarios (simulada)
base_de_datos_usuarios = {
    "usuario1": "contrasenia1",
    "usuario2": "contrasenia2",
    "usuario3": "contrasenia3"
}

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

def ingresar_cliente():
    cedula = input("Ingrese el número de cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    return Cliente(cedula, nombre)

def login():
    while True:
        # Solicitar credenciales al usuario
        usuario = input("Ingrese su nombre de usuario: ")
        contrasenia = input("Ingrese su contraseña: ")

        # Verificar si las credenciales son válidas
        if usuario in base_de_datos_usuarios and base_de_datos_usuarios[usuario] == contrasenia:
            print("Inicio de sesión exitoso. Bienvenido,", usuario)
            break
        else:
            print("Credenciales inválidas. Por favor, inténtelo de nuevo.")

def valideVacios(valor):
    return valor.strip() != ""

def gestion_datos():
    print("Gestión de datos en proceso...")
    cliente = ingresar_cliente()
    print("\nDatos del cliente:")
    print("Cédula:", cliente.cedula)
    print("Nombre:", cliente.nombre)

def pedido_mesas_comidas():
    print("Pedido de mesas y comidas en proceso...")
    
    # Total de mesas reservadas
    total_mesas = reservacion_mesas()
    
    # Total de ventas realizadas
    total_ventas = realizar_ventas()
    
    # Total general
    total_general = total_mesas + total_ventas
    
    # Datos de la factura
    cliente = ingresar_cliente()
    print("\nFactura:")
    print("Cliente:", cliente.nombre)
    print("Cédula:", cliente.cedula)
    print("Total general: $", total_general)

def reservacion_mesas():
    # Declaración de variables
    num_mesas = int(input("Indique la cantidad de mesas: "))
    precio_mesas = 0

    # Bucle para solicitar y acumular
    for i in range(num_mesas):
        precio_mesas += int(input("¿Cuánto cuesta cada mesa " + str(i + 1) + ": "))

    # Condición de precio
    if precio_mesas <= 7500:
        descuento = precio_mesas * 0.30
        precio_mesas -= descuento
    elif precio_mesas > 11000:
        descuento = precio_mesas * 0.10
        precio_mesas -= descuento
        print("Esta reservación tiene un descuento de:", descuento)

    # Fuera del bucle
    print("El total de las mesas es:", precio_mesas)
    return precio_mesas

def mostrar_menu_productos():
    # Menú de productos y precios
    productos = {
        "1": {"nombre": "Casado", "precio": 10},
        "2": {"nombre": "Olla de carne", "precio": 8},
        "3": {"nombre": "Costilla a la diabla", "precio": 12}
    }

    # Mostrar el menú de productos
    print("Menú de productos:")
    for clave in productos:
        producto = productos[clave]
        print(clave + ". " + producto["nombre"] + "- $" + str(producto["precio"]))

def realizar_ventas():
    total_venta = 0
    opcion = ""  # Se inicializa la variable opcion

    # Mostrar menú de productos
    mostrar_menu_productos()

    # Realizar ventas
    while opcion != "0":
        opcion = input("Seleccione el producto (1/2/3) o '0' para finalizar la venta: ")
        productos = {
            "1": {"nombre": "Casado", "precio": 10},
            "2": {"nombre": "Olla de carne", "precio": 8},
            "3": {"nombre": "Costilla a la diabla", "precio": 12}
        }

        if opcion in productos:
            cantidad = int(input("Cantidad de " + productos[opcion]["nombre"] + " vendidos: "))
            total_venta += productos[opcion]["precio"] * cantidad
            print("Venta registrada.")
        elif opcion == "0":
            print("Venta finalizada.")
        else:
            print("Opción inválida.")

    # Mostrar total de la venta y generar factura
    print("El total de las ventas es: $", total_venta)
    return total_venta

def main():
    continuar = True
    while continuar:
        # Menú principal
        print("\n--- Menú ---")
        print("1. Gestión de datos")
        print("2. Pedido de mesas y comidas")
        print("3. Salir")
        
        opc = input("Seleccione una opción: ")

        if valideVacios(opc):
            opc = int(opc)
            if opc >= 1 and opc <= 3:
                if opc == 1:
                    gestion_datos()
                elif opc == 2:
                    pedido_mesas_comidas()
                elif opc == 3:
                    print("Hasta luego")
                    continuar = False
                else:
                    print("Opción inválida. Intente nuevamente.")
        else:
            print("Debe ingresar un valor válido.")

if __name__ == "__main__":
    login()
    main()





