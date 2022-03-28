def notas(* infos, sit=False):
    resultado = dict()

    resultado['total'] = len(infos)
    resultado['maior'] = max(infos)
    resultado['menor'] = min(infos)
    resultado['media'] = sum(infos)/len(infos)
    if sit:
        if resultado['media'] < 5:
            resultado['situacao'] = 'RUIM'
        elif 5 <= resultado['media'] < 7:
            resultado['situacao'] = 'MEDIANO'
        elif 7 <= resultado['media'] < 9:
            resultado['situacao'] = 'BOM'
        else:
            resultado['situacao'] = 'EXCELENTE'

    return resultado


print(notas(9, 10, 5.5, 2.5, 8.5 , sit=True))