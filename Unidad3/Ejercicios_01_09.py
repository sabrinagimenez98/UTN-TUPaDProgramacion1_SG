#Ejercicio FOR

#corrimiento=int(input("Lugares a correr: "))

corrimiento=2
letra_alterna=[]
lista=[]
#integrantes=int(input("Cuantos integrantes son?: "))
integrantes=0
for i in range (integrantes):
    i=i+1
    palabra=str(input("Palabra: "))
    for letra in palabra:
        clave=chr(ord(letra) + corrimiento)
        letra_alterna.append(clave)
    letra_alterna.append(" / ")

resultado="".join(letra_alterna)

print(f"Las nuevas claves son: {resultado}")

#Ejercicio WHILE

import random
opciones = ["piedra","papel","tijera"]
compu= random.choice(opciones)

contador=0
jugadas=0

while contador==0:
    jugador=input("Que vas a sacar (piedra,papel o tijera)?: ")
    if jugador==("piedra" or "papel" or "tijera"):
        print("Eligio correctamente")
        print(f"Jugador: {jugador} vs Computadora:{compu}")
    else:
        print("El jugador introdujo una opcion incorrecta")
        contador=3
    

if jugador==compu:
    print("Empate")
elif (jugador=="piedra" and compu=="tijera")or(jugador=="papel" and compu=="piedra") or (jugador=="tijera" and compu=="papel"):
      j1=1
      print("Gana el Jugador")
      #Gana Jugador
elif (compu=="piedra" and jugador=="tijera")or(compu=="papel"and jugador=="Piedra")or(compu=="tijera"and jugador=="papel"):
    c1=1
    #Gana Computadora
    print("Gana la Computadora")

