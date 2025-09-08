import random
numeros = random.sample(range(1, 51), 25)
filas=5
columnas=5
carton= [[random.choice(numeros) for _ in range(columnas)] 
 for _ in range(filas)]

for i in range(5):
    print(carton[i])

matriz_0=[[[0 for _ in range(columnas)] 
           
 for _ in range(filas)]]
while carton==matriz_0:
    num_aleatorio=random(1,51)
    