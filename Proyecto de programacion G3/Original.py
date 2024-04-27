import datetime

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
    clientes = []  
    for i in range(cantidad_clientes):
        print("\nCliente", i+1)
        cliente = ingresar_cliente()
        clientes.append(cliente)  
        print("\nDatos del cliente:")
        print("Cédula:", cliente.cedula)
        print("Nombre:", cliente.nombre)
    return clientes

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
        # Lista de mesas disponibles
        mesas_disponibles = list(range(1, 13))
        
        # Solicitar número de mesa al cliente
        while True:
            num_mesa = int(input("Ingrese el número de mesa que desea reservar (1-12): "))
        
            # Verificar si la mesa está disponible
            if num_mesa in mesas_disponibles:
                mesas_disponibles.remove(num_mesa)
                precio_mesa = 1000  # Precio de la mesa
                total_cuenta = precio_mesa  # Total de la cuenta
                print("¡Mesa reservada exitosamente!")
                break
            else:
                print("Lo siento, esta mesa ya está reservada.")
                continue
        
        # Aplicar descuentos según el precio de la mesa
        descuento = 0
        if total_cuenta <= 7500:
            descuento = total_cuenta * 0.30
            total_cuenta -= descuento
            print(f"Esta reservación tiene un descuento de {descuento}")
        elif total_cuenta > 11000:
            descuento = total_cuenta * 0.10
            total_cuenta -= descuento
            print(f"Esta reservación tiene un descuento de {descuento}")

        # Fecha y hora de reservación
        fecha_reserva = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
        hora_reserva = input("Ingrese la hora de la reserva (HH:MM): ")

        # Total de ventas realizadas
        total_ventas = realizar_ventas()
        
        # Cálculo del impuesto
        impuesto = total_cuenta * 0.13
        
        # Total general con impuestos
        total_general = total_cuenta + total_ventas + impuesto
        
        print("\nFactura:")
        print("Cliente:", nombre_cliente)
        print("Cédula:", cedula_cliente)
        print("Fecha de reserva:", fecha_reserva)
        print("Hora de reserva:", hora_reserva)
        print("Número de mesa reservada:", num_mesa)
        print("Total sin impuestos: $", total_cuenta)
        print("Impuesto (13%): $", impuesto)
        print("Total general: $", total_general)

        print("\n¡Su comida y mesa están listas y reservadas!")
    else:
        print("Este cliente no se encuentra disponible. Vuelva a intentarlo.")

def realizar_ventas():
    total_venta = 0
    opcion = ""  

    mostrar_menu_productos()

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

    print("El total de las ventas es: $", total_venta)
    return total_venta

def mostrar_menu_productos():
    productos = {
        "1": {"nombre": "Casado", "precio": 10},
        "2": {"nombre": "Olla de carne", "precio": 8},
        "3": {"nombre": "Costilla a la diabla", "precio": 12}
    }

    print("Menú de productos:")
    for clave in productos:
        producto = productos[clave]
        print(clave + ". " + producto["nombre"] + "- $" + str(producto["precio"]))

def main():
    continuar = True
    clientes = []  
    while continuar:
        print("\n--- Menú ---")
        print("1. Gestión de datos")
        print("2. Pedido de mesas y comidas")
        print("3. Salir")
        
        opc = input("Seleccione una opción: ")

        if valideVacios(opc):
            opc = int(opc)
            if opc >= 1 and opc <= 3:
                if opc == 1:
                    clientes = gestion_datos()  
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