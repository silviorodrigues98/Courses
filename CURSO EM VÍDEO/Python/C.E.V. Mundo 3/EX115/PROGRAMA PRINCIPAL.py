from EX115.dados import (criar_arquivo,
                         ler_dados,
                         adicionar_dado, )
from time import sleep
from EX115 import formatações

arquivo = criar_arquivo("cadastro_completo.xlsx")
while True:
    formatações.print_linhas("MENU PRINCIPAL")
    formatações.print_cores("""O que deseja fazer? 
[1] Listar dados 
[2] Cadastrar novo
[3] Sair do cadastro """, "azul")
    formatações.linhas("-")
    while True:
        try:
            formatações.print_cores("Sua opção", "verde")
            opcoes = int(input(""))
            if opcoes == 1 or opcoes == 2 or opcoes == 3:
                break
            else:
                formatações.print_cores("ERRO!Digite uma opção válida", "vermelho")
        except:
            formatações.print_cores("ERRO!Digite uma opção válida", "vermelho")
    if opcoes == 1:
        formatações.print_linhas("PESSOAS CADASTRADAS")
        dados = ler_dados(arquivo, linhaInicial=2)
        tam = len(dados[0])
        if tam == 0:
            formatações.print_cores("Ainda não há cadastros no sistema. ", "amarelo")
        cont = 0
        while cont < tam:
            print(f"{dados[0][cont]:<22}{dados[1][cont]} anos")
            cont += 1
    elif opcoes == 2:
        formatações.print_linhas("NOVO CADASTRO")
        linha = ler_dados(arquivo, colunaInicial=1, linhaInicial=1)
        final = len(linha[0]) + 1
        nome = str(input("Nome: ").strip().title())
        adicionar_dado(arquivo, nome, "A", final)
        linha = ler_dados(arquivo, colunaInicial=2, colunaFinal=2, linhaInicial=1)
        final = len(linha[0])
        while True:
            try:
                idade = int(input("Idade: "))
                adicionar_dado(arquivo, idade, "B", final)
                print(f"Novo registro de {nome} adicionado.")
                break
            except :
                formatações.print_cores("ERRO! Por favor digite um número inteiro válido. ", "vermelho")
    elif opcoes == 3:
        break
    else:
        formatações.print_cores("ERRO!Digite uma opção válida! ", "vermelho")
formatações.print_linhas("Saindo do sistema... Até logo! "), sleep(1.5)
