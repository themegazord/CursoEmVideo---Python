a = float(input('Insira o tamanho do lado A: '))
b = float(input('Insira o tamanho do lado B: '))
c = float(input('Insira o tamanho do lado C: '))

if abs(a-b) < c < a + b and abs(a-c) < b < a + c and abs(b-c) < a < b + c:
    if a == b == c:
        print('Equilatero')
    elif a != b != c != a:
        print('Escaleno')
    elif (a == b) != c or (b == c) != a or (a == c) != b:
        print('Isósceles')
else:
    print('Não forma um triangulo')



