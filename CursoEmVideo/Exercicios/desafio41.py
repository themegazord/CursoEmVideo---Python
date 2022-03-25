from datetime import datetime
y = int(input('Informe o ano de nascimento do atleta: '))
dy = datetime.now().year - y

if dy <= 9:
    print('MIRIM')
elif 9 < dy <= 14:
    print('INFANTIL')
elif 14 < dy <= 19:
    print('JUNIOR')
elif 19 < dy <= 25:
    print('SÊNIOR')
elif dy > 25:
    print('MASTER')