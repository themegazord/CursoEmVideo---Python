a = int(input('Digite um ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Ano bissexto')
else:
    print('O ano não é bissexto')
