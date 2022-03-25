from math import pow
a = float(input('Informe a sua altura, em centimetros: '))
p = float(input('Informe seu peso: '))

imc = p / pow(a, 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbita')