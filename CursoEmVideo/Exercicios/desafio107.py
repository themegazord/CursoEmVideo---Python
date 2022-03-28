from modulo107 import moeda

n = float(input('Insira um valor: R$'))

print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'Aumentando 10% de {n} teremos {moeda.aumentar(n, 10)}')
print(f'Reduzindo 13% de {n} teremos {moeda.diminuir(n, 13)}')