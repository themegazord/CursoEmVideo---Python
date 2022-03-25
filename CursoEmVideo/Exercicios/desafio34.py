s = float(input('Qual seu salário? '))
print('Seu salario é de R${:.2f}' .format(s + (s * 0.1))) if s > 1250 else print('Seu salário é R${:.2f}' .format(s + (s * .15)))