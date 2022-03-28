from .. import interface


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        interface.cabecalho('PESSOAS CADASTRADAS')
        print(f'{"Nome"}\t\t\t\t\t\t\t{"Idade"}')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]}\t\t\t\t\t\t\t{dado[1]} \tanos')


def gravarArquivos(nome):
    try:
        a = open(nome, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        interface.cabecalho('CADASTRO DE PESSOAS')
        linha = list()
        nome = str(input('Digite o nome: ')).strip()
        idade = int(input('Digite a idade: '))
        linha.append(nome + ';' + str(idade)+'\n')
        try:
            a.write(f'{nome};{idade}\n')
        except TypeError as erro:
            print(f'Erro ao escrever no arquivo -> {erro}')
        else:
            print(f'Dado de {nome} foi inserido no banco de dados!')
            del linha
            a.close()