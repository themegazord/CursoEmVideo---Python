nome = input('Insira seu nome: ')
print('Analisando seu nome...')
split = nome.split()
ne = ''.join(split)
print('Seu nome todo maiusculo é: {}'.format(nome.upper()))
print('Seu nome todo minusculo é: {}' .format(nome.lower()))
print('Seu nome, sem espaços tem {} letras' .format(len(ne)))
print('Seu primeiro nome tem {} letras' .format(len(split[0])))


