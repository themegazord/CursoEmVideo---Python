a = float(input('Insira o comprimento do lado A: '))
b = float(input('Insira o comprimento do lado B: '))
c = float(input('Insira o comprimento do lado C: '))

if abs(b-c) < a < (b + c) and abs(a-c) < b < (a + c) and abs(a-b) < c < (a+b):
    print('Pode montar um triangulo!!!')
else:
    print('Não forma um triangulo!!!')