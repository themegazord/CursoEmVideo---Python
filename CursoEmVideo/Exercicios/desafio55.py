p = []
ma = 0;
me = 0;
for c in range(1, 6):
    p.append(float(input('Insira o valor do {}º peso: ' .format(c))))
ma += p[0]
me += p[0]
for c in range(0, len(p)):
    if p[c] > ma:
        ma = p[c]
    if p[c] < me:
        me = p[c]
print('O maior peso é: {:.2f}Kg'.format(ma))
print('O menor peso é: {:.2f}Kg'.format(me))