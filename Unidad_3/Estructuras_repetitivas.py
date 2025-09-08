#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.
# Solicitar número al usuario

numero_digitos = int(input("Ingresá un número entero: "))
# Convertir a positivo si es negativo
if numero_digitos < 0:
    numero_digitos = -numero_digitos
# Contar dígitos usando repetición
digitos = 0
while numero_digitos > 0:
    numero_digitos = numero_digitos // 10
    digitos += 1
print(digitos)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

valor_inicial=int(input("Ingrese el Valor inicial: "))
valor_final=int(input("Ingrese el Valor final: "))
suma=0
for i in range(valor_inicial+1,valor_final):
    suma += i
print(suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

suma = 0
while True:
    numero_secuencia = int(input("Ingresá un número entero (0 para cortar): "))
    if numero_secuencia == 0:
        print("Programa terminado")
        break
    suma += numero_secuencia
    print("La suma total es:",suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0, 9)
numero_usuario=0
cont=0
while numero_usuario!=numero_aleatorio:
    numero_usuario=int(input("Adivine el numero: "))
    cont += 1
print("ADIVINASTE EL NUMERO!!!!")
print("Intentos necesarios para adivinar:",cont)

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i, end=' ')

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

numero_p = -1
while numero_p <= 0:
    numero_p = int(input("Ingresá un número entero positivo: "))
    if numero_p <= 0:
        print("El número debe ser mayor que cero. Intentá de nuevo ")
suma = 0
for i in range(0,numero_p + 1):
    suma += i
print("La suma de los números desde 0 hasta", numero_p, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares=0
impar=0
#Para cambiar la cantadad de numeros a procesar cambio el valor de la valiriable cantadad_num
cantidad_num=10
for i in range (1,cantidad_num):
    numero_a_evaluar=int(input(f"Ingrese el numero entero {i}: "))
    if numero_a_evaluar%2==0:
        pares += 1
    else:
        impar +=1
print("La cantidad de numeros pares es:",pares,"y de numeros impares:",impar)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

#Para cambiar la cantadad de numeros a procesar cambio el valor de la valiriable cantadad_numeros
cantidad_numeros=10
suma = 0

for i in range(1,cantidad_numeros+1):
    numero = int(input(f"Ingresá el número {i}: "))
    suma += numero

media = suma / cantidad_numeros
print("La media de los 10 números ingresados es:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresá un número entero: ")
numero_invertido = ""

for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]

print("Número invertido:", numero_invertido)
