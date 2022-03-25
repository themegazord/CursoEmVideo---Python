p = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
     'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for w in p:
    print(f'\nNa palavra {w.lower()} temos ', end='')
    for l in w:
        if l.lower() in 'aeiou':
            print(l.lower(), end=' ')