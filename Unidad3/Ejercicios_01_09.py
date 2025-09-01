
#corrimiento=int(input("Lugares a correr: "))

#palabra="abcde"
corrimiento=2
letra_alterna=[]
lista=[]
integrantes=int(input("Cuantos integrantes son?: "))

for i in range (integrantes):
    i=i+1
    palabra=str(input("Palabra: "))
    for letra in palabra:
        clave=chr(ord(letra) + corrimiento)
        letra_alterna.append(clave)
        resultado="".join(letra_alterna)
        lista.append(" "+ resultado)

print(lista)
