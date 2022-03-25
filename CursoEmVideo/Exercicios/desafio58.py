from random import randint
pc = randint(1, 10)
t = 0
u = int(input('Tente adivinhar em qual número a máquina está pensando de 1 a 10: '))
while pc != u:
    u = int(input('Você errou, tente novamente.'))
    t += 1
print('Você acertou, parabens')
print('Você tentou {} vezes até acertar :D' .format(t))