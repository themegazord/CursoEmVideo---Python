temp = dict()
dados = list()
soma = media = 0
while True:
    temp['nome'] = str(input('Nome: ')).strip()  # Nome
    sexo = str(input('Sexo: [M/F] ')).strip()  # Sexo
    while sexo not in 'MmFf':  # Verifica se foi realmente informado F ou M
        print('ERRO! Por favor informe apenas F ou M')
        sexo = str(input('Sexo: [M/F] ')).strip()
    temp['sexo'] = sexo  # insere sexo dentro do dict
    temp['idade'] = int(input('Idade: '))  # idade
    soma += temp['idade']
    usr = str(input('Dseja continuar? [S/N]')).strip()  # usuario quer continuar
    while usr not in 'SsNn':  # verifica se realmente a pessoa quer continuar com o programa
        print('ERRO! Por favor, insira apenas S ou N')
        usr = str(input('Deseja continuar? [S/N]'))
    dados.append(temp.copy())
    if usr in 'Nn':
        break
media = soma / len(dados)
print('-=-'*30)
print(f'A) Ao todo, temos {len(dados)} pessoas cadastradas.')
print(f'B) A de idade das {len(dados)} pessoas cadastradas é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for i in dados:
    if i['sexo'] in 'Ff':
        print(i['nome'], end=' ')
print(f'\nD) As pessoas com idade acima da média são: ')
for i in dados:
    if i['idade'] > media:
        print(f'Nome: {i["nome"]}; Sexo: {i["sexo"].upper()}; idade: {i["idade"]}')