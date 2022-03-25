bd = list()
usr = list()

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    usr.append(nome)
    usr.append(peso)
    bd.append(usr[:])
    usr.clear()

    decision = str(input('Quer continuar? [S / N]'))
    if decision in 'Nn':
        break
#Maior e menor peso
maiorp = menorp = bd[0][1]
for pos, p in enumerate(bd):
    if bd[pos][1] > maiorp:
        maiorp = bd[pos][1]
    elif bd[pos][1] < menorp:
        menorp = bd[pos][1]
#Pegar o nome do caboclo
print(f'O maior peso foi {maiorp:.2f}Kg. Peso de', end=' ')
for n in bd:
    if n[1] == maiorp:
        print(f'{n[0]}', end=' ')
print(f'\nO menor peso foi {menorp:.2f}Kg. Peso de', end=' ')
for n in bd:
    if n[1] == menorp:
        print(f'{n[0]}', end=' ')

