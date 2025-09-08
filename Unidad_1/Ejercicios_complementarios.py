#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1=int(input("Escribe un numero entero: "))

#2. No borres la variable número uno y crea una variable llamada "numero2" asignándole 
#un número decimal de tu elección
numero2=float(input("Escribe un numero decimal: "))

#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma= numero1+numero2
print(f"La suma es {suma}")

#4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para 
#multiplicación y otra para división. Imprime estas variables.
resta = numero1-numero2
print(f"La resta es {resta}")
multiplicacion= numero1*numero2
print(f"La multiplicacion es {multiplicacion}")
division= numero1/numero2
print(f"La division es {division}")

#5. Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre=str(input("Dime tu nombre: "))

#6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el 
#precio de un artículo ficticio.
precio=float(input("Dime el precio del articulo: "))

#7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
#un valor decimal que represente el descuento aplicado al artículo.
descuento=float(input("Dime el descuento: "))

#8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y 
#almacena el resultado en una variable llamada "precio_final".
precio_final=precio*(100-descuento)/100
print(f"El precio final es {precio_final}")

#9. Crea una variable llamada "cadena" y asignale un texto, una frase, etc.
cadena=str(input("Dime una algo: "))
print(f"Me dijiste {cadena}")

#10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas 
#a almacenar la longitud en caracteres de la cadena.
longitud=len(cadena)
print("Esa frase tiene una longitud de {longitud}")

#11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y 
#conviértelo en número entero.
preciodecimal=float(input("Dime un precio decimal: "))
precioentero =int (preciodecimal)
print("De forma entera seria {precioentero}")

#12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas 
#en una tercera variable llamada "nombre_completo", el nombre y el apellido con un 
#espacio entre medio.
nombre=str(input("Dime tu nombre: "))
apellido=str(input("Dime tu apellido: "))
nombre_completo=nombre + " " + apellido
print(f"Tu nombre completo es: {nombre_completo}")

#13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad=int(input("Dime tu edad: "))
despues=edad+5
antes=edad-10
print(f"Hace 10 años tenias {antes}")
print(f"En 5 años tendras {despues}")

#14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y 
#centímetros.
altura=float(input("Dime tu altura en metros y centimetros: "))
alto= altura*4
bajo= altura/3
print(f"Tu altura es {altura} pero si fuera el cuadruple seria {alto} y si fuera un tercio de su altura {bajo}")

#15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después 
#transfórmalo todo en minúsculas con algún método o función de Python.
nombreMayu=str(input("Dime tu nombre: "))
text=nombreMayu
nomMayuscula = text.upper()
nomMinuscula = text.lower()
print(f"Tu nombre en Mayusculas es: {nomMayuscula}") 
print(f"Tu nombre en Minusculas es: {nomMinuscula}")

#16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido 
#para que se transforme todo en minúsculas excepto la primera letra.
nombreformal= text.capitalize()
print("Normalmente seria {nombreformal}")