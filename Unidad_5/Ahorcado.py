import random

# Lista de palabras
palabras = ["python", "programacion", "organizacion", "arquitectura"]

# Selección aleatoria
palabra_secreta = random.choice(palabras)
intentos = ["_"] * len(palabra_secreta)
letras_adivinadas = []
intentos_restantes = 6

def mostrar_tablero():
    print("Palabra:", " ".join(intentos))
    print(f"Intentos restantes: {intentos_restantes}")

def procesar_letra(letra):
    global intentos_restantes
    if letra in letras_adivinadas:
        print("Ya intentaste esa letra.")
    elif letra in palabra_secreta:
        print("Correcto! La letra está en la palabra.")
        for i, l in enumerate(palabra_secreta):
            if l == letra:
                intentos[i] = letra
        letras_adivinadas.append(letra)
    else:
        print("Incorrecto. La letra no está en la palabra.")
        letras_adivinadas.append(letra)
        intentos_restantes -= 1

# Juego principal
print("Bienvenido al juego del ahorcado!")
while "_" in intentos and intentos_restantes > 0:
    mostrar_tablero()
    letra = input("Ingresa una letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa una sola letra válida.")
        continue
    procesar_letra(letra)

# Resultado final
if "_" not in intentos:
    print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
else:
    print(f"Has perdido. La palabra era: {palabra_secreta}")
