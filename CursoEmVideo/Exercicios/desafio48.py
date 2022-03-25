s = 0
count = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        count += 1
        s += c

print('A soma de todos os {} solicitados foi {}' .format(count, s))
