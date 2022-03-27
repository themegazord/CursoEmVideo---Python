txt = ['Gustavo de Camargo Campos', 'Curso em Python', 'CeV']
def escreva(t):
    l = len(t) + 6
    print('~'*l)
    print(f'   {t}')
    print('~'*l)
for i in txt:
    escreva(i)