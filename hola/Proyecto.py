"""
Proyecto de programacion

Estudiantes encargado:
Jefferson Aguilar Mendoza
Juan Pablo Vergara Cholele
Jonatan Pereira Guevara
Geovanna Castro Sanchez


Univesidad Fidelitas
"""


#Declaracion de variables
descuento= 0
num_Mesas= 0
precio_Mesas= 0
total_Cuenta= 0
orden=0

#datos
print("menu:")
print("1.casado")
print("2.olla de carne")
print("3.costilla a la diabla")


pedidos=int(input("cuantas ordenes desea realizar:"))
if pedidos==1:
    orden=int(input("digite la opcion del menu que desea ordenar"))
    print("orden recibida en la cocina")
    print("su orden estara lista en 5 minutos")

else:
    if pedidos==2:
        orden=int(input("digite la opcion del menu que desea ordenar"))
        print("orden recibida en la cocina")
        print("su orden estara lista en 5 minutos")
    else:
        if pedidos==3:
            orden=int(input("digite la opcion del menu que desea ordenar"))
            print("orden recibida en la cocina")
            print("su orden estara lista en 5 minutos")


#Solicitud de datos
num_Mesas=int(input("Indique la cantidad de mesas"))

#Bucle para solicitar y acumular
for i in range (num_Mesas):
    precio_Mesas=int(input("Cuanto cuesta cada mesa" +str(i+1)+": "))

#Condicion de precio
if(precio_Mesas<=7500):
    descuento=precio_Mesas*0.30
    precio_Mesas=precio_Mesas-descuento
    print("Esta reservacion tiene un descuento de  "+str(i+1)+": ",precio_Mesas)

elif (precio_Mesas>11000):
    precio_Mesas=precio_Mesas-descuento
    print("Esta reservacion tiene un descuento de  "+str(i+1)+": ",precio_Mesas)
total_Cuenta=total_Cuenta+precio_Mesas #Acumulador


#Fuera del Bucle
print("La factura en total  ", total_Cuenta)

