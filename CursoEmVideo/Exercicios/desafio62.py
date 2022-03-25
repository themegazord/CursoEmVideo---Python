n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
termo = n
t = 0
c = 1
op = 10
while op != 0:
    t += op
    while c <= t:
        print('{} => '.format(termo), end='')
        termo += r
        c+=1
    print('PAUSE')
    op = int(input('Quantos termos a mais você quer ver? '))
print('Você verificou {} termos' .format(t))
