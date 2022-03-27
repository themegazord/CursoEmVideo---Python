dados = dict()
gols = list()
total = 0
dados['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input('Quantas partidas ele jogou na temporada? '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i + 1}: ')))
for i in gols:
    total+=i
dados['gols'] = gols.copy()
dados['total'] = total
print('-=-'*30)
print(dados)
print('-=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i in range(0, len(gols)):
    print(f'{"=>":>7} Na partida {i+1}, fez {gols[i]}.')
print(f'Foi um total de {dados["total"]} gols.')
