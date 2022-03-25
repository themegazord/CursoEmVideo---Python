from random import randint
pc = randint(1, 5)
n = int(input('Insira um número de 1 a 5 e veja se consegue prever a máquina: '))
print('MAQUINA: Hmmm... Eu escolho {}' .format(pc))
print('Parabens' if n == pc else 'Que pena você perdeu.')