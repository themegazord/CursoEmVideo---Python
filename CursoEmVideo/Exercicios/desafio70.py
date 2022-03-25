m1000 = 0
n = str(input('Informe o nome do produto: ')).strip()
p = float(input('Valor: R$'))
s = b = p
nb = n
while True:
    valid = str(input('Deseja inserir mais um produto? [S/N] '))
    if valid in 'Nn':
        break
    n = str(input('Informe o nome do produto: ')).strip()
    p = float(input('Valor: R$'))
    s += p
    if p > 1000:
        m1000+=1
    if p < b:
        b = p
        nb = n
print(f'O total gasto dos produtos foi: R${s:.2f}\n{m1000} produto(s) tem o valor maior de R$1.000\nO produto mais barato é {nb} e seu valor é de R${b:.2f}')
