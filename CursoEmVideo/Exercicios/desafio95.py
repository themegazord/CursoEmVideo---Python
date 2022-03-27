jogadores = list()
gols = list()
temp = dict()
while True:
    temp['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {temp["nome"]} jogou? '))
    for i in range(1, partidas + 1):
        gols.append(int(input(f'{" ":<5}Quantos gols na partida {i}: ')))
    temp['gols'] = gols[:]
    totalGols = 0
    for i in gols:
        totalGols += i
    temp['total'] = totalGols
    gols.clear()
    usr = str(input('Deseja continuar? [S/N] ')).strip()
    while usr not in 'SsNn':
        print('ERRO! Insira apenas S ou N')
        usr = str(input('Deseja continuar? [S/N] ')).strip()
    jogadores.append(temp.copy())
    if usr in 'Nn':
        break
print('-='*24)
print(f'{"Código":<8}{"Nome":<20}{"Gols":<15}{"total"}')
'''print(jogadores)'''
for pos, i in enumerate(jogadores):
    print(f'{str(pos):<8}{i["nome"]:<20}{str(i["gols"]):<15}{i["total"]}')
print('-='*24)
op = int(input('Deseja ver os dados especificos de algum jogador? [999 para sair] '))
while True:
    if op == 999:
        break
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR: {jogadores[op]["nome"]}')
        for pos, i in enumerate(jogadores):
            if op == pos:
                for j, g in enumerate(i['gols']):
                    print(f'{" ":<5} No jogo {j + 1} fez {g} gols')
    op = int(input('Deseja ver os dados especificos de algum jogador? [999 para sair] '))

