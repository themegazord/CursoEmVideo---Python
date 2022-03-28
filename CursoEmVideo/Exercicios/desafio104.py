def leiaInt():
    n = input('Digite um número: ').strip()
    while True:
        if n.isnumeric() != True:
            print('\033[1;31mERRO! Informe um número valido!!!\033[m')
            n = input('Digite um número: ').strip()
        else:
            break
    print(f'Você acabou de digitar o número: {n}')

leiaInt()
