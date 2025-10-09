#Mochila Dora la exploradora

while True:
    try:
        tamaño_mochila=int(input("Ingrese el tamaño de la mochila: "))
        if tamaño_mochila > 0:
            print(f"El número {tamaño_mochila} es válido.")
            break  # Sale del bucle si el número es positivo
        else:
            print("El número debe ser positivo. Inténtalo de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

opc=0

while opc!=5:
    print("\nMenu de la mochila")
    print("1.Guardar objeto.")
    print("2.Ver mochila.")
    print("3.Eliminar objeto.")
    print("4.Salir del programa.")

    opc=input("\nIngrese una opcion: ")
    while not opc.isdigit():
        opc=input("\nOpcion invalida. Ingrese un número de 1 al 8: ")
        continue
    opc=int(opc)

   # match opc: case 1: case 2: case 3: case 4: case _:
