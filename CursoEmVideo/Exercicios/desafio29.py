v = float(input('Insira a velocidade: '))
if v > 80:
    m = (v - 80) * 7
    print('Você ultrapassou {} Km/h do permitido que é 80Km/h, você será multado em: R${:.2f}' .format(v - 80, m))
else:
    print('Pode prosseguir')
