def leiaDinheiro():
    valido = False
    while not valido:
        n = str(input('Digite o preço: R$')).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print(f'\033[1;31mERRO! \"{n}\" é um preço inválido\033[m')
        else:
            valido = True
            return float(n)
