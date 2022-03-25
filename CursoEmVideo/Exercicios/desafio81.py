lista = list()
count = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    count += 1
    usr = str(input('Quer continuar? [S / N]'))
    if usr in 'Nn':
        break
lista.sort(reverse=True)
five = "faz parte" if 5 in lista else "não faz parte"
print(f'Você digitou {count} elementos')
print(f'Os valores em ordem decrescente são {lista}')
print(f'O valor 5 {five} da lista')