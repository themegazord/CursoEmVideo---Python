from random import randint
jogos = list()
temp = list()
qtd = int(input('Digite quantos jogos serão feitos: '))
for i in range(0, qtd):
    for j in range(0,6):
        temp.append(randint(1,60))
    jogos.append(temp[:])
    temp.clear()
print('Seus jogos foram feitos: ')
for i in jogos:
    print(i, '\n')
