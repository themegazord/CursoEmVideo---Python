def fatorial(n, show=False):
    """
    -> Função fatorial irá realizar o fatoramento da variavel n.
    :param n: Valor a ser fatorado - OBRIGATÓRIO
    :param show: Caso False, apresentará apenas o resultado, se True, mostrará passo a passo do calculo
    :return: Retorna o resultado da fatoração.
    """
    f = 1
    if show == False:
        for i in range(n, 0, -1):
            f *= i
        return f
    else:
        for i in range(n, 0, -1):
            f *= i
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
    return f

help(fatorial)