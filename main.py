import interfaz
import random

def leer_palabra_secreta(palabras):
    palabra = random.choice(palabras)
    return palabra

def pedir_letra(letras_usadas):
    while True:
        letra = input("Ingrese una letra: ").lower()
        if letra.isalpha() and len(letra) == 1 and letra not in letras_usadas:
            letras_usadas.append(letra)
            return letra
        else:
            print("Entrada inválida, por favor ingrese una letra del abecedario que no haya sido usada antes.")

def verificar_letra(letra, palabra_secreta):
    return letra in palabra_secreta

def validar_palabra(letras_usadas, palabra_secreta):
    for letra in palabra_secreta:
        if letra not in letras_usadas:
            return False
    return True


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de una lista.
    palabras = ["listas", "bucles", "variables"]
    palabra_secreta = leer_palabra_secreta(palabras)
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')