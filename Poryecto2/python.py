import random

def adivina_el_numero(x):

    print("===========================")
    print("Bienvenido(a) al Juego")
    print("===========================")
    print("Tu meta es adivinar el número generado por la computadora ")


    numero_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y x.

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) #f-string

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")

    print(f"Felicitaciones! Adivinaste el número {numero_aleatorio} correctamente")

adivina_el_numero(10)