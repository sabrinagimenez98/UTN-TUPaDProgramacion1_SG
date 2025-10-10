#1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
#print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330  ● Manzana = 1700 ● Melón = 2800
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
#print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
# en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

#Supongo que la lista debe estar en el diccionario ya creado

precios_frutas["Sin precio"] = ["Mandarina","Sandia","Frutilla"]
#print(precios_frutas)


#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos={}
cantidad_contactos=0
for i in range(cantidad_contactos):
    contacto=input(f"Nombre del contacto {i+1}: ").title()
    numero=input(f"Numero {contacto}: ")
    contactos[contacto]=numero
print(contactos)

# Buscar un número por nombre

#consulta = input("\nIngresá el nombre del contacto que querés buscar: ").title()
#if consulta in contactos:
#    print(f"El número de {consulta} es: {contactos[consulta]}")
#else:
#    print(f"No se encontró el contacto {consulta}")


#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

#frase=input("Escribe una frase con repeticiones: ").title()
frase="hola mundo hola"

palabras=frase.split() #Separo las palabras en una lista

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"Palabras únicas: {palabras_unicas}")
print(f"Frecuencia de palabras: {recuento}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
cantidad_alumnos=3
notas_por_alumno=3
for i in range(cantidad_alumnos):
    alumno=input(f"Nombre del contacto {i+1}: ").title()
    for i in range(notas_por_alumno):
        nota=input(f"Nota {i+1}: ")
        
    contactos[contacto]=numero

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron P1 y P2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.
