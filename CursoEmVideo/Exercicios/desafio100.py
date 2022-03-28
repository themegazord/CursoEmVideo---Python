from random import randint
from time import sleep

numeros = list()


def sorteia():
    print('Sorteando os números', end='')
    for d in range(0, 3):
        sleep(1)
        print('.', end='')
    print()
    linhas()
    for i in range(0, 5):
        numeros.append(randint(1, 10))
    for j in numeros:
        sleep(.75)
        print(f'{j} ', end=' ')
    print('foram os números sorteados!!!')

def somaPar(num):
    linhas()
    print(f'Analisando os números {num}', end='')
    for d in range(0, 3):
        sleep(1)
        print('.', end='')
    print('\n')
    print('Os números pares são: ', end='')
    for p in num:
        if p % 2 == 0:
            sleep(.75)
            print(f'{p}', end=' ')
    somar = 0
    for i in num:
        if i % 2 == 0:
            somar += i
    print(f'e a soma deles é {somar}')


def linhas():
    print('-='*30)


sorteia()
somaPar(numeros)