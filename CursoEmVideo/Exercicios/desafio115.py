from modulo115.interface import *
from modulo115.arquivo import *
from time import sleep
arq = 'bancodedados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Programa'])
    if resposta == 1:
        gravarArquivos(arq)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('ERRO! Digite uma opção válida')
    sleep(2)