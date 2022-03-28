def l ():
    print('-'*30)


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def aumentar(n, j, form=False):
    if form:
        s = n * (j/100)
        return moeda(n+s)
    else:
        s = n * (j / 100)
        return n + s


def diminuir(n, j, form=False):
    if form:
        s = n * (j / 100)
        return moeda(n - s)
    else:
        s = n * (j / 100)
        return n - s


def metade(n, form=False):
    if form:
        return moeda(n / 2)
    else:
        return n / 2


def dobro(n, form=False):
    if form:
        return moeda(n*2)
    else:
        return n * 2


def resumo(n, jmais, jmenos):
    nf = moeda(n)
    l()
    print(f'{"RESUMO DO VALOR":^30}')
    l()
    print(f'Preço analisado:\t{nf}')
    print(f'Dobro do preço:\t\t{dobro(n, True)}')
    print(f'Metade do preço:\t{metade(n, True)}')
    print(f'{jmais:.0f}% de aumento:\t\t{aumentar(n, jmais, True)}')
    print(f'{jmenos:.0f}% de desconto:\t{diminuir(n, jmenos, True)}')
    l()
