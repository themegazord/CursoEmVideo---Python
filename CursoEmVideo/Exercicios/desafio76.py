prod = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25,
        'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
        'Canetas', 22.3, 'Livro', 34.9)
sum = 0
print('-' * 40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-' * 40)
for pos, p in enumerate(prod):
    if pos % 2 == 0:
        print(f'{p}{"." * (30 - len(p))}', end='')
    elif pos % 2 != 0:
        print(f'R$ {prod[pos]:>7.2f}')
print('-' * 40)
for s in prod:
    if prod.index(s) % 2 != 0:
        sum += s

print(f'{"Valor Total":.<30}R${sum:>8.2f}')
