#1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200 ● Manzana = 1500 ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330  ● Manzana = 1700 ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
# en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

#Supongo que la lista debe estar en el diccionario ya creado

precios_frutas["Sin precio"] = ["Mandarina","Sandia","Frutilla"]
print(precios_frutas)


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

consulta = input("\nIngresá el nombre del contacto que querés buscar: ").title()
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto {consulta}")


#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase=input("Escribe una frase con repeticiones: ").title()
#frase="hola mundo hola" Frase prueba

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
alumnos={}
for i in range(cantidad_alumnos):
    nombre_alumno=input(f"Nombre del alumno {i+1}: ").title()
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre_alumno}: ")) for j in range(notas_por_alumno))
    alumnos[nombre_alumno]=notas
print(alumnos)

print("\nPromedios de los alumnos:")
for nombre_alumno,notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre_alumno}:{promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron P1 y P2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Sets de estudiantes que aprobaron cada parcial
print("\n")
parcial1 = {"Sabri", "Isma", "Ares"}
parcial2 = {"Sabri","Isma","Joaquin"}

#& → intersección (ambos parciales)
#^ → diferencia simétrica (solo uno)
#| → unión (todos sin repetir)

# Estudiantes que aprobaron ambos parciales
ambos = parcial1 & parcial2
# Estudiantes que aprobaron solo uno de los dos
solo_uno = parcial1 ^ parcial2
# Estudiantes que aprobaron al menos un parcial (sin repetir)
al_menos_uno = parcial1 | parcial2

print("✅ Aprobados en ambos parciales:", ambos)
print("🟡 Aprobados en solo uno de los dos:", solo_uno)
print("📋 Aprobados en al menos uno:", al_menos_uno)

#Use la IA pero me sirvio para entender como usar intersección,diferencia y unión

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

productos_libreria= {"lapicera": 20,"cuaderno": 15,"resaltador": 10}
opc=0
while opc!=5:
    print("\nMenú de opciones")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto")
    print("3. Agregar nuevo producto")
    print("4. Mostrar catalogo completo")
    print("5. Salir")

    opc=input("\nIngrese una opcion: ")
    while not opc.isdigit():
        opc=input("\nOpcion invalida. Ingrese un número de 1 al 8: ")
        continue
    opc=int(opc)
    match opc:
        case 1: 
            producto= input("Ingresá el nombre del producto: ").lower()
            if producto in productos_libreria:
                print(f"{producto}: {productos_libreria[producto]} unidades")
            else:
                print(f"El producto {producto} no se ha encontrado.")

        case 2:
            producto = input("Ingresá el nombre del producto: ").lower()
            if producto in productos_libreria:
                unidades = int(input(f"Cuántas unidades quieres agregar a {producto}?: "))
                productos_libreria[producto] += unidades
                print(f"Nuevo stock de {producto}: {productos_libreria[producto]} unidades")
            else:
                print(f"El producto {producto} no existe.")

        case 3:
            producto = input("Ingresá el nombre del nuevo producto: ").lower()
            if producto in productos_libreria:
                print(f"El producto {producto} ya existe.")
            else:
                unidades = int(input(f"Cuántas unidades tiene {producto}?: "))
                productos_libreria[producto] = unidades
                print(f"Producto {producto} agregado con {unidades} unidades.")

        case 4:
            print("\nCatalogo completo")
            print(productos_libreria)

        case 5:
            print("Salio del menu de opciones. Gracias por utilizarlo")
            break

        case _:
            print("Opción inválida. Elegir un numero entre 1 y 4.")


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

agenda={}
cant_event=int(input("Ingresa la cantidad de eventos que quieres crear: "))

for i in range(cant_event):
    evento=input(f"Ingrese nombre del evento n°{i+1}: ")
    dia=int(input(f"Ingrese dia del evento {evento}: "))
    hora=int(input(f"Ingrese hora del evento {evento}: "))
    agenda[evento]=(dia, hora)

consulta_dia=int(input("\nIngresá el día que querés consultar: "))
consulta_hora=int(input("Ingresá la hora que querés consultar: "))
evento=agenda.get((consulta_dia, consulta_hora))

if evento:
    print(f"El día {consulta_dia} a las {consulta_hora} hs hay: {evento}")
else:
    print(f"No hay eventos registrados para el día {consulta_dia} a las {consulta_hora} hs")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

#Diccionario Paises: Capitales
mapa_1={"Argentina":"Bs As",
    "Chile":"Santiago de Chile",
    "Perú":"Lima"}
print("\nDiccionario paises:capitales")
print(mapa_1)

#Diccionario Capitales: Paises
mapa_2={}

for clave in mapa_1.keys():
    mapa_2[mapa_1[clave]]=clave
print("\nDiccionario capitales:paises")
print(mapa_2)