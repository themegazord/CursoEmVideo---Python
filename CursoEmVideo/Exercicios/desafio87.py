matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
sum3col = sumvalpar = maival2lin = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor da coordenada [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            sumvalpar += matriz[i][j]
        if j == 2:
            sum3col += matriz[i][j]
        if i == 1 and matriz[i][j] > maival2lin:
            maival2lin = matriz[i][j]

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print(f'A soma de todos os valores pares são: {sumvalpar}')
print(f'A soma de todos os valores da 3º coluna é: {sum3col}')
print(f'O maior valor da 2º linha é: {maival2lin}')