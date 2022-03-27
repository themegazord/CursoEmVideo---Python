def l():
    print('-'*30)


def calculaTerreno(l, c):
    t = l * c
    print(f'A área de um terreno de {l} x {c} é de {t}m².')


print('Controle de terrenos')
l()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
calculaTerreno(l, c)