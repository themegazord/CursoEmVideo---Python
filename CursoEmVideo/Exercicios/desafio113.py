def leiaInt():
    while True:
        try:
            n = (int(input('Digite um Inteiro: ')))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: valor inserido não é um INTEIRO\033[m')
        else:
            return n


def leiaFloat():
    while True:
        try:
            n = (float(input('Digite um valor Real: ')))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: valor inserido não é um REAL\033[m')
        else:
            return n


inteiro = leiaInt()
real = leiaFloat()
print(f'O valor inteiro digitado foi {inteiro}')
print(f'O valor real digitado foi {real}')

