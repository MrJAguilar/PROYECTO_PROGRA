class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

def ingresar_cliente():
    cedula = input("Ingrese el número de cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    return Cliente(cedula, nombre)

def main():
    num_clientes = int(input("Ingrese el número de clientes: "))
    clientes = []

    for i in range(num_clientes):
        print(f"\nCliente {i + 1}:")
        cliente = ingresar_cliente()
        clientes.append(cliente)

    print("\nListado de clientes ingresados:")
    for i, cliente in enumerate(clientes):
        print(f"\nCliente {i + 1}:")
        print("Cédula:", cliente.cedula)
        print("Nombre:", cliente.nombre)
        
    print("\nBienvenidos al restaurante Sabor y Tradición")

if __name__ == "__main__":
    main()