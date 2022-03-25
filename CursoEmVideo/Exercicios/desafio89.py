from math import ceil
turma = list()
aluno = list()
notas = int(input('Digite quantas notas cada aluno terá: '))
nota = list()
while True:
    aluno.append(str(input('Nome: ')))
    for c in range(0, notas):
        aluno.append(float(input(f'Nota {c + 1}: ')))
    turma.append(aluno[:])
    aluno.clear()
    usr = str(input('Deseja continuar [S / N]? '))
    if usr in 'Nn':
        break
        print('-='*30)
#Mostra tabela de notas
print(f'No', f' Nome', f'{"Media":>20}')
print('-'*30)
for pos, i in enumerate(turma):
    somaNotas = 0
    for j in range(1, notas + 1):
        somaNotas += turma[pos][j]
    print(f'{pos:<3} {turma[pos][0]:<20} {(somaNotas / notas):<1.1f}')
#Mostra notas por escolha
cond = int(input('Mostrar notas de qual aluno? (Digite 999 para sair)'))
while cond != 999:
    for pos, i in enumerate(turma):
        if cond == pos:
            for j in range(1, notas + 1):
                nota.append(turma[pos][j])
            print(f'Notas de {turma[pos][0]} são {nota}')
            nota.clear()

    cond = int(input('Mostrar notas de qual aluno? (Digite 999 para sair)'))
    if cond == 999:
        break
print('-'*30)
print('Fim do programa, volte sempre!!!')



