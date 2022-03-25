print('='*10, 'MEGA LOJAS', '='*10)
v = float(input('Informe o valor da compra: R$'))
print('\n[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] em até 2x no cartão\n[4] 3x ou mais no cartão')
dd = v - (v * 0.10)
dc = v - (v * 0.05)
j = v + (v * 0.20)
r = int(input('Informe sua opção de pagamento: '))
'''elif r == 4:
    x = int(input('Quantas vezes será passado: '))
    print('')
    '''

if r == 1:
    print('Total das compras: R${:.2f} -> Opção com desconto de 10%\nValor total a pagar: R${:.2f}' .format(v, dd))
elif r == 2:
    print('Total das compras: R${:.2f} -> Opção com desconto de 5%\nValor total a pagar: R${:.2f}' .format(v, dc))
elif r == 3:
    print('Total das compras: R${:.2f} -> Opção com parcelamento em 2x\nValor total a pagar: R${:.2f}\nValor parcelado: 2x de R${:.2f}' .format(v, v, v/2))
elif r == 4:
    x = int(input('Quantas vezes será passado: '))
    print('Total das compras: R${:.2f} -> Opção com parcelamento em {}x e juros de 20%\nValor total a pagar: R${:.2f}\nValor parcelado: {}x de R${:.2f}'.format(v, x, j, x,(j/x)))