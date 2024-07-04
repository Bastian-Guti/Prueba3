import random
import csv
cliente = []

def registrar_pedido():
    ids=random.randrange(1000,9999)
    nombre,apellido,direccion = input("Nombre:"),input("Apellido:"),input("Direccion:")

    comunaN =input("Seleccione a que comuna pertenece\n(1)Concepción\n(2)Chiguayante\n(3)Talcahuano\n(4)Hualpén\n(5)San Pedro")

    while True:
        litros10 = 0+0
        litros20 = 0+0
        litros6 = 0+0
        if comunaN == "1":
            comuna = "Concepción"
            break
        elif comunaN == "2":
            comuna = "Chiguayante"
            break
        elif comunaN == "3":
            comuna = "Talcahuano"
            break
        elif comunaN == "4":
            comuna = "Hualpén"
            break
        elif comunaN == "5":
            comuna = "San Pedro"
            break
        else:
            print("Numero invalido ingrese otro")

    while True:
        pedido = input("Que dispensadores desea llevar\n(1)6 Litros\n(2)10Litros\n(3)20 Litros\n(4)Salir")
        if pedido == "1":
            litros6 = int(input("Cuantos dispensadores desea:"))
        elif pedido == "2":
            litros10 = int(input("Cuantos dispensadores desea:"))      
        elif pedido == "3":
            litros20 = int(input("Cuantos dispensadores desea:"))
        elif pedido == "4":
            print("Saliendo")
            break
        else:
            print("Numero invalido ingrese otro")

    cliente.append({
    "ID":ids,"Nombre":nombre,"Apellido":apellido,"Direccion":direccion,
    "Sector":comuna,"Litro6":litros6,"Litro10":litros10,"Litro20":litros20
    })

def listar_pedidos():
    print("ID pedido  Cliente     Direccion    Sector    Disp.6lts   Disp.10lts   Disp.20lts")
    for client in cliente:
        print(f"ID:{client["ID"]} Nombre y Apellido:{client["Nombre"]} {client["Apellido"]} Direccion:{client["Direccion"]} Sector:{client["Sector"]} Dis.6lts{client["Litro6"]} Dis.10lts{client["Litro10"]} Dis.20lts {client["Litro20"]}")




def hoja_ruta(): 
    while True:
        comunaN = input("Que hoja de ruta Desea\n(1)Concepción\n(2)Chiguayante\n(3)Talcahuano\n(4)Hualpén\n(5)San Pedro") 
        if not cliente:
            ("No hay Clientes")
            break
        else:
            if comunaN == "1":
                comunaN = "Concepción"
                break
            elif comunaN == "2":
                comunaN = "Chiguayante"
                break
            elif comunaN == "3":
                comunaN = "Talcahuano"
                break
            elif comunaN == "4":
                comunaN = "Hualpén"
                break
            elif comunaN == "5":
                comunaN = "San Pedro"
                break
            else:
                print("Numero invalido ingrese otro")

    with open("archivo.csv","w") as f:
        writer = csv.writer(f,delimiter=" ")
        for client in cliente:
            if comunaN == client["Sector"]:
                writer.writerow(f"ID:{client["ID"]} Nombre y Apellido:{client["Nombre"]} {client["Apellido"]} Direccion:{client["Direccion"]} Sector:{client["Sector"]} Dis.6lts{client["Litro6"]} Dis.10lts{client["Litro10"]} Dis.20lts {client["Litro20"]}")



def busca_ID():

    for client in cliente:
        print(f"ID:{client["ID"]}")

    num= int(input("ID desea ver:"))

    for client in cliente:
        if num == client["ID"]:
            print(f"ID:{client["ID"]} Nombre y Apellido:{client["Nombre"]} {client["Apellido"]} Direccion:{client["Direccion"]} Sector:{client["Sector"]} Dis.6lts{client["Litro6"]} Dis.10lts{client["Litro10"]} Dis.20lts {client["Litro20"]}")
    
        


def main():
    while True:
        num = input("Escriba el numero que desea ingresar\n(1)Registrar Pedido\n(2)Listar Pedido\n(3)Hoja de Ruta\n(4)Busacar ID del Pedido\n(5)Salir\n")
        if num == "1":
            registrar_pedido()
        elif num =="2":
            listar_pedidos()
        elif num=="3":
            hoja_ruta()
        elif num =="4":
            busca_ID()
        elif num == "5":
            break
        
        



if 1==1:
    main()