'''cont = 1
while True:
    print(cont, ' -> ' ,end='')
    if cont == 55:
        break
    cont+=1
print('Acabou')'''

'''n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}' .format(s))
print(f'A soma vale {s}')
'''

'''nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')'''
resp = str(input('a:' )).strip().upper()[0]
print(resp)