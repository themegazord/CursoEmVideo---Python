n1 = float(input('Insira a nota 1: '))
n2 = float(input('Insira a nota 2: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[1;31;40mReprovado\033[m')
elif 5 <= m <= 6.9:
    print('\033[1;34;40mRecuperação\033[m')
elif m > 6.9:
    print('\033[1;32;40mAprovado\033[m')
