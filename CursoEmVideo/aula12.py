nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil!')
elif nome in ('Ana Claudia Jéssica Juliana'):
    print('Seu nome é bem feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}' .format(nome))