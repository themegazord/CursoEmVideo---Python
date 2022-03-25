l = list()
while True:
    n = int(input('Digite um valor: '))
    if n in l:
        print('Valor duplicado! Não vou adicionar')
    elif n not in l:
        l.append(n)
        print('Valor inserido com sucesso')
    usr = str(input('Quer continuar? '))
    l.sort()
    if usr in 'Nn':
        print(l)
        break




