from random import randint
from time import sleep
numeros = []
def sorteia():
    print('SORTEANDO OS VALORES DA LISTA: ', end="")
    for x in range(0, 5):
        num = randint(0, 10)
        print(num, end=" ")
        sleep(.5)
        numeros.append(num)
    print("feito!")

def somaPar():
    total = 0
    for x in numeros:
        if x % 2 == 0:
            total += x
    print(f"Somando os valores pares de {numeros}, temos {total}.")

sorteia()
somaPar()