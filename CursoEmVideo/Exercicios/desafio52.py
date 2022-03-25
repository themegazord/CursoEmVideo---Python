n = int(input('Digite um número: '))
count = 0;
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        count += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisivel {} vezes' .format(n, count))
if count == 2:
    print('\033[mO número {} é primo.'.format(n))
else:
    print('\033[mO número {] não é primo'.format(n))