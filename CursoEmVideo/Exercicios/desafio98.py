from time import sleep
def contador(inicio, fim, cont):
    print(f'Contagem de {inicio} até {fim} de {cont} em {cont}')
    if inicio < fim:
        for i in range(inicio, fim + cont, cont):
            print(i, end=' ')
            sleep(1)
        print('\n')
    else:
        for i in range(inicio, fim - cont, -cont):
            print(i, end=' ')
            sleep(1)
        print('\n')


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Inicio: '))
f = int(input('Fim: '))
c = int(input('Contagem: '))
contador(i, f, c)