from time import sleep


def linha():
    print('-=' * 30)


def maior(*n):
    m = n[0]
    for i in n:
        if i > m:
            m = i
    linha()
    print('Analisando os valores passados', end='')
    for i in range(0, 3):
        sleep(1)
        print('.', end='')
    print(f'\nOs números inseridos na chamada foram ', end='')
    for j in n:
        print(j, end=' ')
        sleep(.75)
    print(f'e o maior número é {m}')

maior(2, 9, 4, 5, 7, 1)
maior(3,6,4)
maior(4,9)
maior(0)