somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
count = 0
for p in range(1, 5):
    print('-'*10, ' {}º PESSOA ' .format(p), '-'*10)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        count += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos' .format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos' .format(nomevelho, maioridadehomem))
print('Existem {} mulher(es) com menos de 20 anos.' .format(count))
