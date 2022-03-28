from modulo107 import moeda

n = float(input('Insira um valor: R$'))
nf = moeda.moeda(n)
print(f'A metade de {nf} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {nf} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10% de {nf} teremos {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Reduzindo 13% de {nf} teremos {moeda.moeda(moeda.diminuir(n, 13))}')