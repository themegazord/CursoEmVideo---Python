from math import cos, tan, sin, radians

x = float(input('Insira um angulo em radianos: '))

print('\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}' .format(cos(radians(x)), sin(radians(x)), tan(radians(x))))