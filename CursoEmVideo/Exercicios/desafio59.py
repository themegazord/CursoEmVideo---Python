op = 0;
print('=' * 10, 'Programa do tio Mega', '=' * 10)
print('Insira 2 valores: ')
a = int(input('Valor A: '))
b = int(input('Valor B: '))
while op != 5:
    print('Escolha um das opções abaixo: ')
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ]Sair do programa')
    op = int(input('Qual sua opção? -> '))

    if op == 1:
        print('A soma do valor A {} com valor B {} é: {}'.format(a, b, a + b))
    elif op == 2:
        print('A multiplicação do valor A {} com valor B {} é: {}'.format(a, b, a * b))
    elif op == 3:
        if a > b:
            print('O número A {} é maior que o número B {}'.format(a, b))
        elif a < b:
            print('O númeor A {} é menor que o número B {}'.format(a, b))
    elif op == 4:
        print('Insira os novos números: ')
        a = int(input('Valor A: '))
        b = int(input('Valor B: '))
print('Fim do programa!!!')
