aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
elif aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'

print('-='*30)
for k, v in aluno.items():
    print(f'{"-":>5}{k:<2} é igual a {v}')