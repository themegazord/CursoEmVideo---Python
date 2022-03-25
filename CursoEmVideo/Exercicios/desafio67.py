while True:
    n = int(input('Que ver a tabuada de qual número? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
