num = int(input('Insira até que termo você deseja ver na sequência de Fibonacci: '))
c = 2
n = 1
na = 1
print('0 -> 1 ->', end=' ')
while c < num:
    print('{} ->' .format(n), end=' ')
    n = na + n
    na = n - na
    c += 1
print('FIM')