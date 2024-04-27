
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
    cantidad_clientes = int(input("Ingrese la cantidad de clientes: "))
    clientes = []  # Lista para almacenar los clientes registrados
    for i in range(cantidad_clientes):
        print("\nCliente", i+1)
        cliente = ingresar_cliente()
        clientes.append(cliente)  # Agregar cliente a la lista
        print("\nDatos del cliente:")
        print("Cédula:", cliente.cedula)
        print("Nombre:", cliente.nombre)
    return clientes  # Devolver la lista de clientes registrados

def pedido_mesas_comidas(clientes):
    print("Pedido de mesas y comidas en proceso...")
    
    # Verificar si el cliente está registrado
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cedula_cliente = input("Ingrese la cédula del cliente: ")
    cliente_encontrado = False
    for cliente in clientes:
        if cliente.nombre == nombre_cliente and cliente.cedula == cedula_cliente:
            cliente_encontrado = True
            break
    
    if cliente_encontrado:
        # Total de mesas reservadas
        num_mesas = int(input("Indique la cantidad de mesas a reservar: "))
        precio_mesas = int(input("Ingrese el monto total para las mesas: "))  # Precio total para todas las mesas

        # Condición de precio
        if precio_mesas < 1500 * num_mesas:
            print("El monto total debe ser igual o mayor al precio de las mesas.")
            return
        
        # Total de ventas realizadas
        total_ventas = realizar_ventas()
        
        # Total general
        total_general = precio_mesas + total_ventas
        
        # Datos de la factura
        print("\nFactura:")
        print("Cliente:", nombre_cliente)
        print("Cédula:", cedula_cliente)
        print("Total general: $", total_general)
    else:
        print("Este cliente no se encuentra disponible. Vuelva a intentarlo.")

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

def main():
    continuar = True
    clientes = []  # Lista para almacenar los clientes registrados
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
                    clientes = gestion_datos()  # Actualizar la lista de clientes registrados
                elif opc == 2:
                    pedido_mesas_comidas(clientes)
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





