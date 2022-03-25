from datetime import datetime
aposentadoria = idade = 0
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip()
pessoa['nasc'] = int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho: (0 não tem) '))
if pessoa['ctps'] != 0:
    pessoa['anoContratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = int(input('Salário: '))
    idade = datetime.now().year - pessoa['nasc']
    tempoDeContribuicao = datetime.now().year - pessoa['anoContratacao']
    if tempoDeContribuicao < 30:
        pessoa['tempoServiço'] = (30 - tempoDeContribuicao) + (58 - idade)

print('-=-' * 30)
for k, v in pessoa.items():
    print(f'O campo {k} contem {v}')
