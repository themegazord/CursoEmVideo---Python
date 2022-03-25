n = float(input('Digite a distância da viagem: '))
if n < 200:
    print('Sua viagem irá custar: R${:.2f}' .format(n * 0.5))
else:
    print('Sua viagem irá custar: R${:.2f}' .format(n * 0.45))