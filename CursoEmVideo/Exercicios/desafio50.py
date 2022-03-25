s = 0
for c in range(1, 7):
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        s += n
print('A soma dos valores pares inseridos é: {}' .format(s))
