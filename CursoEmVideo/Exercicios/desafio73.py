time = ('Atletico Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza',
        'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'América MG',
        'Atlético GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
        'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio',
        'Bahia', 'Sport', 'Chapecoense')
print('='*20)
print('Os 5 primeiros colocados do Brasileirão 2021 Série A são:')
print(time[:5])
print('='*20)
print('Os 4 últimos colocados do Brasileirão 2021 Série A são:')
print(time[-4:])
print('='*20)
print('Os times em ordem alfabética:')
print(sorted(time))
print('='*20)
print('Localização do time Chapecoense: ')
print(f'O time da Chapecoence está na posição {time.index("Chapecoense")+1}º')