"""
Ventas y Facturación
"""

#Declaración de variables
total_venta = 0
opcion = "" # Se inicializa la variable opcion

#Menú de productos y precios
productos = {
  "1": {"nombre": "Casado", "precio": 10},
  "2": {"nombre": "Olla de carne", "precio": 8},
  "3": {"nombre": "Costilla a la diabla", "precio": 12}
}

#Mostrar el menú de productos
print("Menú de productos:")
for clave in productos:
  producto = productos[clave] # Se corrige el nombre de la variable
  print(clave + ". " + producto["nombre"] + "- $" + str(producto["precio"]))

#Realizar ventas
while opcion != "0":
  opcion = input("Seleccione el producto (1/2/3) o '0' para finalizar la venta: ")
  if opcion in productos:
    cantidad = int(input("Cantidad de " + productos[opcion]["nombre"] + " vendidos: "))
    total_venta += productos[opcion]["precio"] * cantidad
    print("Venta registrada.")
  elif opcion == "0": # Se corrige la comparación, debe ser con "0" como cadena
    print("Venta finalizada.")
  else:
    print("Opción inválida.")

#Mostrar total de la venta y generar factura
print("Total de la venta: $" + str(total_venta))
print("Factura generada.")
