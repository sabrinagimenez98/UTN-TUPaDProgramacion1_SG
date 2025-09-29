import random

# Lista de palabras para adivinar
palabras = [
    "python", "tecnologia", "computadora", "programacion", "algoritmo",
    "inteligencia", "variable", "funcion", "robotica", "internet"
]

# Función para seleccionar una palabra al azar
def seleccionar_palabra():
    return random.choice(palabras)

# Función para mostrar el estado actual de la palabra
def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

# Función principal del juego
def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra relacionada con tecnología.")
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))

    while intentos_restantes > 0 and set(letras_adivinadas) != set(palabra_secreta):
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Adivinaste una letra correctamente!")
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

        print(mostrar_tablero(palabra_secreta, letras_adivinadas))

    if set(letras_adivinadas) >= set(palabra_secreta):
        print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
    else:
        print(f"¡Perdiste! La palabra era: {palabra_secreta}")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()
