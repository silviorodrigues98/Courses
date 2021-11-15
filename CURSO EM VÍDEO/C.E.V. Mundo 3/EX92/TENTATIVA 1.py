"""LER NOME, IDADE E CTPS.
DEPOIS CALCULAR SALÁRIO E ANO DE APOSENTADORIA. """
from datetime import datetime


todos_cadastros = []
while True:
    continuar = " "
    pessoa = {"nome": str(input("Qual o nome? >: ")),
              "idade": datetime.now().year - int(input("Ano de nascimento? >; ")),
              "ctps": int(input("Número da CTPS [0 caso não tanha] >: "))}
    if pessoa["ctps"] != 0:
        pessoa["ano_de_contratacao"] = int(input("Ano de contratação >: "))
        pessoa["salario"] = float(input("Salário >:R$ "))
        pessoa["idade_aposentadoria"] = ((pessoa["ano_de_contratacao"] + 35) - datetime.now().year) + pessoa["idade"]
    todos_cadastros.append(pessoa.copy())
    while continuar not in "NnSs":
        continuar = str(input("Deseja adicionar outra pessoa?[S/N] >: ")).upper().strip()[0]
    if continuar in "Nn":
        break
for cada_pessoa in todos_cadastros:
    print()
    for keys, values in cada_pessoa.items():
        print(f" -{keys} tem o valor {values}")
    print("-"*30)
