preco = float(input('Insira o valor que vai obter 15% de desconto: '))
d = preco - (preco * 0.05)

print('O preço R${} caiu para R${} com o desconto de R${}'.format(preco, d, preco*0.05))