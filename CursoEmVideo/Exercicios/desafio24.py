n = input('Digite o nome de alguma cidade: ').strip()
split = n.upper().split()
print('Analisando a palavra...')
r = 'SANTO' in split[0]
print('A cidade {} tem a palavra santo no inicio? {} ' .format(n, r))
