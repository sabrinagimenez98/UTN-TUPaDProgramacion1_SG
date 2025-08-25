#Ejercicio en clase Lunes 25/8
fecha=input("Ingrese el dia de la semana y la fechaben formato DD/MM: ")
print(fecha)
fecha=fecha.split(" ")
auxiliar=fecha[1].strip().split("/")
dia=str(fecha[0])
diaM=dia.upper()
dd=int(auxiliar[0])
mes=int(auxiliar[1])
#Evaluamos el dia
if diaM=="LUNES":
    print("Nivel incial")
elif diaM=="MARTES":
    print("Nivel Intermedio")
elif diaM=="MIERCOLES":
    print("Nivel Avanzado")
elif diaM=="JUEVES":
    print("Practica hablada")
elif diaM=="VIERNES":
    print("Inglés para viajeros")
else:
    print("El dia ingresado no corresponde a un dia de cursado")
#Evaluamos DD y MM
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dd < 30 or dd > 1:
        print ("Evaluamos un mes con 30 dias")
    else:
        print("No es correcto el dia ingresado")
elif mes == 2:
    if dd < 29 or dd > 1:
        print ("Evaluamos un mes con 29 dias")
    else:
        print("No es correcto el dia ingresado")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dd < 31 or dd > 1:
        print ("Evaluamos un mes con 31 dias")
    else:
        print("No es correcto el dia ingresado")
else:
    print("El mes ingresado no es correcto")
if diaM=="LUNES" or diaM=="MARTES" or diaM=="MIERCOLES":
    alum_aprobados=int(input("Ingrese la cantidad de alumnos que aprobaron ese dia: "))
    alum_no_aprobados=int(input("Ingrese la cantidad de NO alumnos que aprobaron ese dia: "))
    total=alum_aprobados+alum_no_aprobados
    porcentaje_aprobados=(alum_aprobados*100)/total
    print(f"El porcentaje de alumnos aprobados es {porcentaje_aprobados}")
else:
    print("Ese dia no se tomaron examenes")