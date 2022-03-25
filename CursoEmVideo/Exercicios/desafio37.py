n = int(input('Insira um número qualquer: '))
print('='*10, 'ESCOLHA PARA CONVERSÃO', '='*10)
print('1 - Binário')
print('2 - Octadecimal')
print('3 - Hexadecimal')
r = int(input('Insira o sua opção: '))

if r == 1:
    print('O número {} em sua forma Binária é {}!!!' .format(n, format(n, "b")))
elif r == 2:
    print('O número {} em sua forma Octadecimal é {}!!!' .format(n , format(n, "o")))
elif r == 3:
    print('O número {} em sua forma Hexadecimal é {}!!!' .format(n, format(n, "x")))
else:
    print('Opção inválida, tente novamente!!!')