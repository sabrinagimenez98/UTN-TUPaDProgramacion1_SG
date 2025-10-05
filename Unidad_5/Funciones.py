#Funciones

# #1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
#“Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimi_hola_mundo():
    print("Hola Mundo!")
    
imprimi_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un 
# nombre y devuelva un saludo personalizado.

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

#nombre=input("Dime tu nombre: ").title()
nombre="Sabri"
saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) 
# que reciba cuatro parámetros e imprima: “Soy[nombre] [apellido], tengo [edad] años y vivo 
# en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre_info,apellido,edad,residencia):
    print(f"Soy {nombre_info} {apellido}, tengo {edad} años y vivo en {residencia}")

#nombre_info=input("Dime tu nombre: ").capitalize()
#apellido=input("Dime tu apellido: ").capitalize()
#edad=input("Dime tu edad: ")
#residencia=input("Dime tu pais de residencia: ").capitalize()

#informacion_personal(nombre_info,apellido,edad,residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como 
# parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar 
# ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    import math 
    area = round(math.pi * (radio ** 2),2)
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = round(2 * math.pi * radio,2)
    return perimetro

radio = float(input("Introduce el radio del círculo: "))

print(f"El area del circulo es {calcular_area_circulo(radio)} y el perimetro es {calcular_perimetro_circulo(radio)}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos 
# como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los 
# segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas= round(segundos/3600,5)
    return horas

segundos=float(input("Segundos a convertir: "))

print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
# y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y 
# llamar a la función.

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros
#  y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y 
# la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario 
# los datos y llamar a la función para mostrar el resultado con dos decimales.

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en
#  grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura 
# en Celsius y mostrar el resultado usando la función.

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como 
# parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.