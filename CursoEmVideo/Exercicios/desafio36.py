c = float(input('Informe o valor da casa: '))
s = float(input('Qual seu salário? '))
p = float(input('Em quantos anos você irá pagar a casa? '))

m = p * 12
pm = c / m
j = s * 0.3

if pm > j:
    print('Você não poderá comprar a casa, infelizmente 30% do seu salário R${:.2f} fica abaixo das parcelas mensais de R${:.2f} dentro do prazo estipulado de {:.0f} anos' .format(s, pm, p))
elif pm <= j:
    print('Parabéns, você irá conseguir financiar a casa em {:.0f}x de R${:.2f}'.format(m, pm))