v = int(input('Insira o valor'))
u = str(input('Você deseja continuar? '))
s = v
c = 1
ma = me = v
while u in 'Ss':
    v = int(input('Insira o valor: '))
    u = str(input('Você deseja continuar? '))
    s += v
    c += 1
    if v > ma:
        ma = v
    else:
        me = v
ms = s/c
print('Você digitou {} números e a média deles foi {}' .format(c, ms))
print('O maior valor foi {} e o menor foi {}' .format(ma, me))

