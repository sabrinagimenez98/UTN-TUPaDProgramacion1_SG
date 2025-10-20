# Dragon = D
# Pared = x
# Camino = o
# Salida = S
laberinto = [
 ["x", "x", "x", "x", "x"],
 ["D", "o", "o", "o", "x"],
 ["x", "o", "x", "o", "S"],
 ["x", "o", "o", "o", "x"],
 ["x", "x", "x", "x", "x"] ]
movimiento=[
 [" ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " "]]

def buscar_salida(laberinto,fila,columna):
    if laberinto[fila][columna]=="S":
        print("Haz salido.")
        return True
    elif laberinto[fila][columna]=="x"or laberinto[fila][columna] in movimiento:
        print("Te chocaste con una pared.")
        return False
    else:
        movimiento[fila][columna]=laberinto[fila][columna]
        if laberinto[fila][columna]=="o":
            print("Vas por buen camino.")
            return True
while True:
    try:
        print("\n==Menu de opciones==")
        print("1.Mover hacia arriba")
        print("2.Mover hacia abajo")
        print("3.Mover hacia la izquierda")
        print("4.Mover hacia la derecha")

        opcion = int(input('Ingrese un opción: '))
        posicion_inicial=laberinto[1][0]

        match opcion:
            case 1:
                fila=+1 
            case 2:
                fila=-1
            case 3:
                columna=-1 
            case 4:
                columna=+1
            case _:
                    print('Opcion incorrecta.')
    except ValueError:
        print('ERROR. Tiene que ingresar un número entero.')



