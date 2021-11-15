""" LISTA COMPOSTA COM NOME E DUAS NOTAS. DEPOIS DAR ALGUNS DADOS SOBRE. """
from time import sleep


lista_completa = []
continuar = " "
contador = 0
while True:
    lista_completa.append([])
    lista_completa[contador].append(str(input("Nome >: ")))
    lista_completa[contador].append([float(input("Nota 1 >: "))])
    lista_completa[contador][1].append(float(input("Nota 2 >: ")))
    lista_completa[contador].append(((lista_completa[contador][1][0]+lista_completa[contador][1][1])/2))
    while continuar not in "SsNn":
        continuar = str(input("Quer cadastrar outro aluno?[S/N] >: ")).upper().strip()[0]
    if continuar in "Nn":
        break
    continuar = " "
    contador += 1
print("-="*40)
print(f"{'No.'} {'NOME':^20} {'MÉDIA':>10}")
print("-"*30)
for posicao, pessoas in enumerate(lista_completa):
    print(f"{posicao} {pessoas[0]:^20} {pessoas[2]:>10.1f}")
while True:
    mais = int(input("Deseja motrar detalhes de qual aluno?[999 interrompe] >: "))
    if mais == 999:
        break
    if mais < len(lista_completa):
        print("-" * 30)
        print(f"Notas de {lista_completa[mais][0]} são: {lista_completa[mais][1]}")
        print("-" * 30)
    else:
        print("Aluno não encontrado no sistema")
print("FINALIZANDO..."), sleep(1.5)
print("<<< VOLTE SEMPRE >>>")
