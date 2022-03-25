n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite um último número: '))

nums = (n1, n2, n3, n4)

print(f'Você digitou os seguintes números: {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(f'O valor 3 apareceu a primeira vez na {nums.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for p in nums:
    if p % 2 == 0:
        print(p, end=' ')
