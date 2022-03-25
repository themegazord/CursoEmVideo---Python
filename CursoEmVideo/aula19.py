'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}')
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 128.7
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

'''brasil = list()
estado1 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf' : 'Mato Grosso do Sul', 'sigla' : 'MS'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in estado.items():
        print()