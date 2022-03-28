from modulo111 import dados
from modulo111 import moeda

n = dados.leiaDinheiro()
jmais = float(input('Informe quanto de juros: '))
jmenos = float(input('Informe quanto de desconto: '))

moeda.resumo(n, jmais, jmenos)