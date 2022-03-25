s = str(input('Digite uma frase: '))
ns = s.replace(' ', '')
si = ns[::-1]
print(ns)
if si.lower() == ns.lower():
    print('A frase {} é um palíndromo!!!' .format(s))
else:
    print('A frase {} não é um palíndromo!!!')