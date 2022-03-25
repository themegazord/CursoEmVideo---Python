from math import sqrt, pow
ca = float(input('Informe o tamanho do cateto adjascente: '))
co = float(input('Informe o tamanho do cateto oposto: '))

h = sqrt(pow(ca, 2) + pow(co, 2))

print('\nCateto Adjascente: {}\nCateto Oposto: {}\nHipotenusa: {}' .format(ca, co, h))