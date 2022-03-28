from datetime import datetime


def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO')
    elif 16 <= idade < 18:
        return print(f'Com {idade} anos: VOTO OPICIONAL')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


a = int(input('Digite seu ano de nascimento: '))
voto(a)
