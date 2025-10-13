opc=0
def mostrar_prod(producto,precio):
    producto=input("Ingrese nombre del producto: ").lower()
    precio=float(input("Ingrese el precio: "))

    import csv
    while precio<0:
        precio=float(input("Ingrese un valor positivo: "))
        continue

    with open("productos.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["producto", "precio"])  # encabezado
        escritor.writerow([producto, precio])

    print("Archivo CSV creado correctamente.")

def agregar_prod(producto,precio):

    producto=input("Ingrese nombre del nuevo producto: ").lower()
    precio=float(input("Ingrese el precio del nuevo producto: "))

    import csv
    with open("productos.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["producto", "precio"])  # encabezado
        escritor.writerow([producto, precio])

    print("Nuevo producto agregado correctamente.")

def eliminar_prod(producto,precio):
    import csv
    with open("productos.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["producto", "precio"])  # encabezado
        escritor.writerow([producto, precio])

    print("Nuevo eliminado correctamente.")

while opc!=4:
    print("\n====== MENÚ DE PRODUCTOS ======")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    print("===============================")

    opc=input("\nIngrese una opcion: ")

    while not opc.isdigit():
        opc=input("\nOpcion invalida. Ingrese un número de 1 al 4: ")
        continue
    opc=int(opc)

    match opc:
        case 1:
            mostrar_prod()
        case 2:
            agregar_prod()
        case 3:
            eliminar_prod()
        case 4:
            print("Saliendo de programa. Gracias por utilizar el sistema")
        case _:
            print("Opcion invalida.Seleccione una opcion de 1 al 4.")