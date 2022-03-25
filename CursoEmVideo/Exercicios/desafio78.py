u = []
for c in range(0, 5):
    u.append(int(input(f'Digite um valor para a posição {c} ')))
    if c == 0:
        mai = men = u[c]
    else:
        if u[c] > mai:
            mai = u[c]
        if u[c] < men:
            men = u[c]

print(f'O maior valor da lista é {mai} e sua posição é ', end='')
for i, v in enumerate(u):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor da lista é {men} e sua posição é ', end='')
for i, v in enumerate(u):
    if v == men:
        print(f'{i}...')
