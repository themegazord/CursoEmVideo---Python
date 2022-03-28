def ficha(nome='', gols=''):
    n = ''
    g = 0
    """
    -> Função irá retornar formatado, qual é o jogador e quantos gols ele fez
    :param nome: OPCIONAL -> Irá mostrar o nome do jogador que passar por esse parametro, caso
    seja passado um valor em branco o nome será retornado como <desconhecido>
    :param gols: OPCIONAL -> Irá mostrar a quantidade de gols que o mesmo realizou, caso seja
    passado um valor em branco, ou algo diferente de um inteiro, será considerado 0
    :return: O retorno  séra uma formatação informando o nome do jogador caso haja e a quantidade de gols
    caso haja.
    """
    if len(nome) != 0:
        n = nome
    else:
        n = '<desconhecido>'
    if gols.isnumeric():
        g = int(gols)

    return print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de gols: ')).strip()

ficha(nome, gols)