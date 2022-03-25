expr = str(input('Digite a expressão: '))
lista = list()
for simb in expr:
    if simb == '(':
        lista.append(simb)
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print(f'Sua expressão é valida')
else:
    print(f'Sua expressão é inválida')
