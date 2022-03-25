n = 1
s = str(input('Digite o sexo de uma pessoa [M/F]: '))
while n == 1:
    if s not in 'MF':
        s = str(input('Dados inválidos, insira novamente: '))
    elif s in 'MF':
        n = 0