def leiaInt():
    while True:
        try:
            n = (int(input(f'\033[1;32mDigite uma opção: \033[m')))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: valor inserido não é um INTEIRO\033[m')
        else:
            return n


def linha(tam=42):
    return '~'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    open("bancodedados.txt", "a")
    cabecalho('MENU PRINCIPAL')
    for pos, i in enumerate(lista):
        print(f'\033[33m{pos + 1}\033[m - \033[34m{i}\033[m')
    opc = leiaInt()
    linha()
    return opc