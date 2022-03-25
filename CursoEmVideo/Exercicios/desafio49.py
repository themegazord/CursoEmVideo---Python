n = int(input('Insira um número: '))
print('='*20, 'TABUADA DO {}' .format(n), '='*20)
for c in range(1, 11):
    print('{} x {} = {}' .format(n, c, n * c))
print('='*20, 'FIM DA TABUADA', '='*20)