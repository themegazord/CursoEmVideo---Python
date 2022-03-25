n = int(input('Insira um número para verificar seu fatorial: '))
c = n
f = 1
formula = '{}! =' .format(n)
while c != 0:
    f = f * c
    if c != 1:
        formula += ' {} x' .format(c)
    elif c == 1:
         formula += ' {} = {}'.format(c,f)
    c -= 1
print(formula)