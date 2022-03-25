from random import randint
c = 0
while True:
    print('=-'*20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 20)

    u = int(input('Digite um valor: '))
    pOrI = str(input('Par ou Ímpar? [P/I] '))

    print('-'*20)

    pc = randint(1,10)
    t = u+pc
    r = t % 2
    valid = "DEU PAR" if r == 0 else "DEU IMPAR"
    if (pOrI in 'Pp' and r == 0 or pOrI in 'Ii' and r != 0):
        print(f'Você jogou {u} e o computador jogou {pc}. Total de {t} {valid}')
        print('-' * 20)
        print('Você VENCEU!\nVamos jogar novamente...')
        c += 1
    elif (pOrI in 'Pp' and r != 0 or pOrI in 'Ii' and r == 0):
        print(f'Você jogou {u} e o computador jogou {pc}. Total de {t} {valid}')
        print('-' * 20)
        break

print(f'GAME OVER! Você venceu {c} vezes')
