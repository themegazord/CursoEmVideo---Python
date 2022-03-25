from time import sleep
from random import randint

print('=' * 10, 'JOKEMPO', '=' * 10)
print('Escolha...\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA')
u = int(input('Qual você escolhe: '))
p = randint(1, 3)

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO')
sleep(1)

j = ['PEDRA', 'PAPEL', 'TESOURA']
print('Você escolheu {} e a máquina escolheu {}' .format(j[u-1], j[p-1]))
if j[u-1] == 'PEDRA' and j[p-1] == 'TESOURA':
    print('Você venceu, parabéns!!!')
elif j[u-1] == 'TESOURA' and j[p-1] == 'PEDRA':
    print('CPU venceu, tente novamente!!!')
elif j[u-1] == 'PEDRA' and j[p-1] == 'PAPEL':
    print('CPU venceu, tente novamente!!!')
elif j[u-1] == 'PAPEL' and j[p-1] == 'PEDRA':
    print('Você venceu, parabéns!!!')
elif j[u-1] == 'PAPEL' and j[p-1] == 'TESOURA':
    print('CPU venceu, tente novamente!!!')
elif j[u-1] == 'TESOURA' and j[p-1] == 'PAPEL':
    print('Você venceu, parabéns!!!')
elif p == u:
    print('EMPATE')
