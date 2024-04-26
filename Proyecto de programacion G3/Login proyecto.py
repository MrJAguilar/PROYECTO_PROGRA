#variables
nombre = 0
cedula = 0
valideVacios = 0

continuar = True
while continuar:
    # Menú principal
    print("\n--- Menú ---")
    print("1. Reservacion de mesas")
    print("2. Gestion de pedidos")
    print("3. Facturacion")
    print("4. Salir")
    opc = input("Seleccione una opción: ")
    if valideVacios(opc):
        opc = int(opc)
        if opc >= 1 and opc <= 3:
            if opc == 1:
                nombre = input("Ingrese su nombre: ")
                cedula = input("Ingrese su cedula : ")
            elif opc == 2:
                #Gestion de pedidos (agrega tu código aquí)
                pass
            elif opc == 3:
                #Facturacion (agrega tu código aquí)
                pass
            elif opc == 4:
                print("Hasta luego")
                continuar = False
            else:
                print("Opción inválida. Intente nuevamente.")