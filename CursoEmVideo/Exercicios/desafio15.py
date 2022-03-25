d = float(input('Quantos dias foram alugados: '))
k = float(input('Quantos Km foram rodados: '))

dp = d * 60
dk = k * 0.15

print('O valor a pagar é de R${}' .format(dp + dk))