ma18 = h = me20 = 0
while True:
    i = int(input('Digite sua idade: '))
    s = str(input('Digite sua sexualidade: [F/M] ')).strip()
    valid = str(input('Deseja continuar: [S/N] ')).strip()
    if i >= 18:
        ma18+=1
    if s in 'Mm':
        h +=1
    if s in 'Ff' and i < 20:
        me20 += 1
    if valid in 'Nn':
        break
print(f'Pessoas com mais de 18 anos: {ma18}\nHomens cadastrados: {h}\nMulheres com menos de 20 anos: {me20}')