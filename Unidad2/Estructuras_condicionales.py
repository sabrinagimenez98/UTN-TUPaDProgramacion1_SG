#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota=float(input("Ingrese su nota: "))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo en Python para evaluar si un número es par o impar

numero_par=float(input("Ingrese un numero par: "))
if numero_par%2==0:
        print("Es par")
else:
        print("Es impar")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad_categoria=int(input("Ingrese su edad para ser categorizada: "))
if edad_categoria<12:
    print("Niño/a")
elif 12<=edad_categoria<18:
    print("Adolescente")
elif 18<=edad_categoria<30:
    print("Adulto")
else:
    print("Adulto mayor")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña=str(input("Ingrese una contraseña: "))
longitud=len(contraseña)
if 8<=longitud<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
from statistics import mode, median, mean
media=mean(numeros_aleatorios)
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
print(f"La media es {media}")
print(f"La moda es {moda}")
print(f"La mediana es {mediana}")
if media>mediana and mediana>moda:
    print("Sesgo positivo o a la derecha")
elif media<mediana and mediana<moda:
    print("Sesgo negativo o a la izquierda")
elif media==mediana==moda:
    print("Sin sesgo")
else :
    print("No hay coincidencias")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

frase=str(input("Ingresa una frase o palabra: "))
if frase[-1].lower() in "aeiou":
    frase=frase + "!"

print("Resultado:", frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.


input("Ingrese su nombre y una opcion 1,2 o 3: ")
print(nombre_opciones)
nombre_opciones=nombre_opciones.split(" ")
nombre_ingresado=nombre_opciones[0]
opcion=int(nombre_opciones[1])
if opcion==1:
    nombre_1=nombre_ingresado.upper()
    print(nombre_1)
elif opcion==2:
    nombre_2=nombre_ingresado.lower()
    print(nombre_2)
elif opcion==3:
    nombre_3=nombre_ingresado.title()
    print(nombre_3)
else:
    print("La opcion ingresada NO es correcta.")

#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla

magnitad=int(input("Ingrese la magnitud del terrermoto: "))
print("Calificacion segun la Escala de Richter:")
if magnitud==3:
    print("Muy Leve")
elif 3<=magnitud<4:
    print("Leve")
elif 4<=magnitud<5:
    print("Moderado")
elif 5<=magnitud<6:
    print("Fuerte") 
elif 6<=magnitud<7:
    print("Muy Fuerte") 
elif magnitud>=7:
    print("Extremo")
else:
    print("No califica en la Escala")
    
#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

info=input("Ingrese en que hemisferio se encuentra (N/S) y su fecha en formato DD/MM: ").split(" ")
hemisferio=info[0].upper()
auxiliar=info[1].split("/")
dia=int(auxiliar[0])
mes=int(auxiliar[1])
if (mes==3 and dia>=21) or mes in [4,5] or (mes==6 and dia<21):
    if hemisferio=="N":
        print("Primavera")
    elif hemisferio=="S":
        print("Otoño")
    else:
        print("La opcion elegida en hemisferico es erronea")
elif (mes==6 and dia>=21) or mes in [7, 8] or (mes == 9 and dia<21):
    if hemisferio=="N":
        print("Verano")
    elif hemisferio=="S":
        print("Invierno")
    else:
        print("La opcion elegida en hemisferico es erronea")
elif (mes==9 and dia>=21) or mes in [10, 11] or (mes==12 and dia<21):
    if hemisferio=="N":
        print("Otoño")
    elif hemisferio=="S":
        print("Primavera")
    else:
        print("La opcion elegida en hemisferico es erronea")
elif (mes==12 and dia>=21) or mes in [1, 2] or (mes==3 and dia<21):
    if hemisferio=="N":
        print("Invierno")
    elif hemisferio=="S":
        print("Verano")
    else:
        print("La opcion elegida en hemisferico es erronea")
        