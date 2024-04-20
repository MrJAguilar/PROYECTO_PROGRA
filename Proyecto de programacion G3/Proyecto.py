"""
Proyecto de programacion

Estudiantes encargado:
Jefferson Aguilar Mendoza
Juan Pablo Vergara Cholele
Jonatan Pereira Guevara
Geovanna Castro Sanchez

Univesidad Fidelitas
"""
# Declaración de variables
descuento = 0
num_mesas = 0
total_cuenta = 0

# Menú
print("Menú:")
print("1. Casado")
print("2. Olla de carne")
print("3. Costilla a la diabla")

# Solicitar órdenes
pedidos = int(input("¿Cuántas órdenes desea realizar? "))
for _ in range(pedidos):
    orden = int(input("Digite la opción del menú que desea ordenar: "))
    print("Orden recibida en la cocina. Su orden estará lista en 5 minutos.")

# Solicitud de datos
num_mesas = int(input("Indique la cantidad de mesas: "))

# Bucle para solicitar y acumular
for i in range(num_mesas):
    precio_mesa = float(input(f"¿Cuánto cuesta la mesa {i + 1}? "))
    # Condición de precio
    if precio_mesa <= 7500:
        descuento = precio_mesa * 0.30
        precio_mesa -= descuento
        print(f"Esta reservación tiene un descuento de {descuento}")
    elif precio_mesa > 11000:
        precio_mesa -= descuento
        print(f"Esta reservación tiene un descuento de {descuento}")
    
    total_cuenta += precio_mesa  # Acumulador

# Fuera del bucle
print("La factura en total es:", total_cuenta)
