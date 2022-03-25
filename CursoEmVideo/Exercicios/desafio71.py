c50 = c20 = c10 = c1 = 0
print('=-' * 20)
print('CAIXA ELETRÔNICO MEGAZORD\nCédulas em caixa: R$50, R$20, R$10, R$1')
print('=-' * 20)
vi = int(input('Valor a ser sacado: R$'))
v = vi
while True:
        if v >= 50:
            c50 = v // 50
            v -= 50 * c50
        if v >= 20:
            c20 = v // 20
            v -= 20 * c20
        if v >= 10:
            c10 = v // 10
            v -= 10 * c10
        if v <= 9:
            c1 = v
            v -= 1 * c1
        break
print(f'O valor R${v} foi devolvido com:\n{c50} notas de 50\n{c20} notas de 20\n{c10} notas de 10\n{c1} notas de 1 real')
