import random

# Crear 25 números únicos para el cartón
numeros = random.sample(range(1, 51), 25)

# Crear matriz 5x5 sin repeticiones
filas = 5
columnas = 5
carton = []
indice = 0
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(numeros[indice])
        indice += 1
    carton.append(fila)

# Mostrar el cartón inicial
print("🎱 Cartón de Bingo:")
for fila in carton:
    print(fila)

# Números a sortear
num_aleatorio = random.sample(range(1, 51), 50)
print("\n Números sorteados:", num_aleatorio)

# Juego: marcar números en el cartón
contador = 25
for evaluador in num_aleatorio:
    print(f"\n Número sorteado: {evaluador}")
    for i in range(filas):
        for j in range(columnas):
            if carton[i][j] == evaluador:
                carton[i][j] = 0
                contador -= 1
                print(" ")
                print("¡Número marcado!")
                for fila in carton:
                    print(fila)

    if contador == 0:
        print("\n ¡Cartón completo!")
        break