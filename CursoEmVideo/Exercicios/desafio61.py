n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
ns = n
c = 1
while c < 10:
    print('{} =>' .format(ns), end=' ')
    ns += r
    c+= 1
print(ns)

