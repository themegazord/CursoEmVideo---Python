from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for num in n:
    print(f'{num}', end=' ')
print(f'\nO maior valor é: {max(n)}')
print(f'O menor valor é: {min(n)}')