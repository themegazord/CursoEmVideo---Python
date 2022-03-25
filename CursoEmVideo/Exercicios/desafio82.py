lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    usr = str(input('Deseja continuar? [S /N] '))
    if usr in 'Nn':
        break

for pos, i in enumerate(lista):
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Os valor da lista principal são: {lista}')
print(f'Os valor pares dessa lista são: {par}')
print(f'Os valor impares dessa lista são: {impar}')
