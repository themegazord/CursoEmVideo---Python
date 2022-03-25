n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
ns = n + (10 - 1) * r
for c in range (n, ns + r, r):
    print('{}'.format(c), end='->')