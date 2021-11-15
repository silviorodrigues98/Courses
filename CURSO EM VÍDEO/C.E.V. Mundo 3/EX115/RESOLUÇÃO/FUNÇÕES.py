def linha(tamanho=42):
    print("-"*tamanho)


def cabecario(texto):
    linha(42)
    print(texto.center(42))
    linha(42)


def leiaint(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem))
        except:
            print(f"""\033[0;31mERRO! O usuário não digitou um número inteiro.
Tente novamente.\033[m""")
        else:
            break
    return inteiro


def menu(lista):
    from EX115.RESOLUÇÃO.PRINCIPAL import cabecario
    cabecario("MENU PRINCIPAL")
    contador = 1
    for item in lista:
        print(f"{contador}-{item}")
        contador += 1
    linha(42)
    opc = int(input("Qual sua opção?"))
    return opc


def arquivoexiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
        print(f"Arquivo {arq} criado com sucesso")
    except:
        print("Houve um erro na criação do arquivo")


def lerarquivo(arq):
    global a
    try:
        a = open(arq, 'rt')
        from EX115.RESOLUÇÃO.PRINCIPAL import cabecario
        cabecario("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3}")
    except:
        print("Erro ao ler o arquivo")
    finally:
        a.close()


def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de adicionar os dados. ")
        else:
            print(f"Novo registo de {nome} realizado com sucesso")
            a.close()


