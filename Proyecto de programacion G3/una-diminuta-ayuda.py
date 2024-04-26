def valideVacios(valida):
    respuesta = False
    if valida != "":
        respuesta = True
    else:
        print("El valor ingresado está vacío")
    return respuesta

# Función para encontrar un producto en la matriz
def encontrarProducto(idProd, catalogo):
    for product in catalogo:
        if product[0] == idProd:
            return product

def mostrarPrecios(catalogo):
    for product in catalogo:
        print("Id Producto:", product[0])
        print("Descripción:", product[1])
        print("Precio:", product[2])
        print("Cantidad:", product[3])

def mostrarMatriz(catalogo):
    for product in catalogo:
        print("Id Producto:", product[0])
        print("Descripción:", product[1])
        print("Precio:", product[2])
        print("Cantidad:", product[3])

# MATRIZ DE PRODUCTOS
catalogoP = [
    ["1", "Arroz", 1995, 0],
    ["2", "Frijoles", 1795, 0],
    ["3", "Atún", 2100, 0],
    ["4", "Salsa de tomate", 2500, 0],
    ["5", "Pasta de Dientes", 2200, 0],
    ["6", "Shampoo", 5500, 0],
    ["7", "Desodorante", 2500, 0],
    ["8", "Cloro", 1000, 0],
    ["9", "Leche", 2800, 0],
    ["10", "Queso crema", 2300, 0],
    ["11", "Paté", 895, 0],
    ["12", "Escoba", 1050, 0],
    ["13", "Cocacola", 2450, 0],
    ["14", "Canelones", 1600, 0],
    ["15", "Nutella", 3000, 0],
    ["16", "Crema de Maní", 3500, 0],
    ["17", "Gomitas", 500, 0],
    ["18", "Jabón de manos", 2550, 0],
    ["19", "Gelatina", 750, 0],
    ["20", "Flan", 850, 0],
    ["21", "Avena", 1895, 0],
    ["22", "Spaghetti", 1150, 0],
    ["23", "Papel higiénico", 3200, 0],
    ["24", "Sirope", 1395, 0],
    ["25", "Harina", 1095, 0]
]

continuar = True
print("Bienvenido al sistema de Supermercados CR")
while continuar:
    print("---Menu---")
    print("1. Ingresar nueva venta")
    print("2. Actualizar inventario")
    print("3. Salir")
    opc = input("Digite la opción necesaria: ")
    if valideVacios(opc):
        opc = int(opc)
        if opc < 1 or opc > 3:
            print("\nValor no válido.\n")
        else:
            if opc == 1:
                nombreCl = input("Ingrese el nombre del cliente: ")
                if valideVacios(nombreCl):
                    mes = input("Ingrese el número del mes en que se realizó la compra: ")
                    if valideVacios(mes):
                        mes = int(mes)
                        if mes > 12 or mes < 1:
                            print("\nValor no válido.\n")
                        else:
                            dia = input("Ingrese el día de la compra: ")
                            if valideVacios(dia):
                                dia = int(dia)
                                if dia > 31 or dia < 1:
                                    print("\nValor no válido.\n")
                                else:
                                    if (mes == 2 and dia > 29) or dia < 1:
                                        print("Febrero tiene un máximo de 28 días (29 en año bisiesto).")
                                    else:
                                        anno = input("Digite el año en el que se realizó la compra: ")
                                        if valideVacios(anno):
                                            anno = int(anno)
                                            if anno < 2022 or anno > 2024:
                                                print("\nValor no válido.\n")
                                            else:
                                                print("Fecha de la compra:", dia, "|", mes, "|", anno)
                                                mostrarMatriz(catalogoP)
                                                opcion = input("Ingrese el id del producto: ")
                                                existe = encontrarProducto(opcion, catalogoP)
                                                if existe:
                                                    cantidadP = input("Ingrese la cantidad a comprar: ")
                                                    cantidadP = int(cantidadP)
                                                    monto_venta = existe[2] * cantidadP
                                                    print("El ingreso por la venta es:", monto_venta)
                                                    existe[3] += cantidadP
                                                    print("Id producto:", existe[0])
                                                    print("Descripción:", existe[1])
                                                    print("Precio:", existe[2])
                                                    print("Cantidad:", existe[3])
                                                else:
                                                    print("Lo siento, el producto no existe en el catálogo de productos.")
            elif opc == 2:
                print("")
            elif opc == 3:
                continuar = False
                print("Saliendo del sistema, hasta luego")
            else:
                print("Opción no válida")
