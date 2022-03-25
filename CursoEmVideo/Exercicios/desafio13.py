sal = float(input('Qual vai ser o salário reajustado? '))
r = sal * 0.15
st = r + sal

print('O salário R${}, recebeu um aumento de R${} (15%) e agora passa a ser R${}'.format(sal, r, st))