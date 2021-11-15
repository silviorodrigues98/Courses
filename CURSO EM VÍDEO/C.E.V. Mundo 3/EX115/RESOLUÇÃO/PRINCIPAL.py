from EX115.RESOLUÇÃO.FUNÇÕES import *
from time import sleep
from EX115.RESOLUÇÃO.ARQUIVO import *

arq = "cursoemvideo.txt"
if arquivoexiste(arq):
    print("Arquivo encontrado com sucesso")
else:
    criarArquivo(arq)

while True:
    cabecario("SISTEMA ARQUIVO V1.O")
    resposta = menu(("LISTAR DADOS", "CADASTRAR PESSOA", "SAIR DO PROGRAMA"))
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecario("NOVO CADASTRO")
        nome = str(input("NOME: "))
        idade = leiaint("IDADE: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecario("Saindo do programa, até logo"), sleep(1)
        break
    else:
        print("ERRO! Selecione opção válida. ")
