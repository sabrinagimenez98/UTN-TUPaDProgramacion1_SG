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

nombre=input("Dime tu nombre: ").title()

saludar_usuario(nombre)

#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) 
# que reciba cuatro parámetros e imprima: “Soy[nombre] [apellido], tengo [edad] años y vivo 
# en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre_info,apellido,edad,residencia):
    print(f"Soy {nombre_info} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_info=input("Dime tu nombre: ").capitalize()
apellido=input("Dime tu apellido: ").capitalize()
edad=input("Dime tu edad: ")
residencia=input("Dime tu pais de residencia: ").capitalize()

informacion_personal(nombre_info,apellido,edad,residencia)

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

radio=float(input("Introduce el radio del círculo: "))

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
def tabla_multiplicar(numero_tabla):
    for i in range(1,11):
        resultado=i*numero_tabla
        print(f"{i} x {numero_tabla} = {resultado}")

numero_tabla=int(input("De que número quieres conocer la tabla de multiplicar: "))

print(f"Tabla de multiplicar del numero {numero_tabla}:")
tabla_multiplicar(numero_tabla)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros
#y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    print(f"El resultado de la suma es {a+b}")
    print(f"El resultado de la resta es {a-b}")
    print(f"El resultado de la multiplicacion es {a*b}")
    if b!=0:
        print(f"El resultado de la resta es {a/b}")
    else:
        print("No se puede realizar la division")
    
a=float(input("Ingrese el primer numero: "))
b=float(input("Ingrese el segundo numero: "))

print("Operaciones basicas")
operaciones_basicas(a,b)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y 
#la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario 
#los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = round(peso / (altura ** 2), 2)
    return imc

peso=float(input("Ingrese su peso en kilogramos: "))
altura=float(input("Ingrese su altura en metros: "))

print(f"Su IMC es {calcular_imc(peso, altura)}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en
#  grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura 
# en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    F=(celsius * 9/5) + 32
    return F

celsius=float(input("Ingrese temperatura en celsius: "))

print(f"{celsius} grados celsius corresponden a {celsius_a_fahrenheit(celsius)} grados fahrenheit")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como 
# parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(num1,num2,num3):
    promedio= round((num1+num2+num3)/3,2)
    return promedio

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))

print(f"El promedio de {num1}, {num2} y {num3} es {calcular_promedio(num1,num2,num3)}")