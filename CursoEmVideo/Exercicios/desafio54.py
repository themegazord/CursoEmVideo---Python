from datetime import datetime
y = []
ma = 0
me = 0
for c in range (1, 8):
    y.append(int(input('Digite o ano da {}ª pessoa: ' .format(c))))
for c in range(0, len(y)):
    if datetime.now().year - y[c] >= 18:
        ma += 1
    else:
        me += 1
print('Tivemos {} pessoas maiores de idade.' .format(ma))
print('Tivemos {} pessoas menores de idade.' .format(me))