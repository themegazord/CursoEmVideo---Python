n = input('Insira seu nome: ').strip()
split = n.split()
print('Seu primeiro nome é: {} e seu último nome é: {}' .format(split[0], split[len(split)-1]))
