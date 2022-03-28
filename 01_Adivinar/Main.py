import random


def Main():
    print("Adivine el numero entre 0 y 100!")
    cantidad_intentos = int(input("Ingrese la cantidad de intentos que desea tener: "))
    Adivinar(cantidad_intentos)

def Adivinar(cantidad_intentos):
    intento = 0
    numeroSecreto = random.randint(0, 100)
    while intento < cantidad_intentos:
        numeroUsuario = int(input("Ingrese el numero: "))
        intento = intento + 1
        if numeroSecreto == numeroUsuario:
            print("Felicidades! Adivino correctamente el numero en " + str(intento) + " intentos!")
            break
        else:
            print("Mala suerte! no era el numero correcto!" + "\nAun le quedan "
                  + str(cantidad_intentos - intento) + " intentos!\n")



Main()