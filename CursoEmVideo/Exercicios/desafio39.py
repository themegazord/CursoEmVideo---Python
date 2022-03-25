from datetime import datetime
y = int(input('Insira o ano em que você nasceu: '))
dy = datetime.now().year - y

if dy >= 18:
    print('Você tem {} anos, aliste-se imediatamente.' .format(dy))
else:
    print('Você tem {} anos e faltam {} anos para seu alistamento obrigatório.' .format(dy, abs(dy - 18)))