numeros = [[], []]
temp = list()
for c in range(0, 7):
    temp.append(int(input(f'Digite o {c + 1}º valor: ')))

for i in temp:
   if i % 2 == 0:
       numeros[0].append(i)
   else:
       numeros[1].append(i)

print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')