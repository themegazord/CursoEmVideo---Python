n = input('Insira uma frase: ').strip().lower()
print('A primeira ocasião da letra A na frase é na posição {} e a ultima ocasião é {} - {}' .format(n.find('a'), n.rfind('a'), len(n)))