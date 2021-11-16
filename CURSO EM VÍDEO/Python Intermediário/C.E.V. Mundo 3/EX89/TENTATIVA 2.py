""" LISTA COMPOSTA COM NOME E DUAS NOTAS. DEPOIS DAR ALGUNS DADOS SOBRE. """


lista_completa = []
continuar = " "
contador = 0
cont = 1
while True:
    lista_completa.append([])
    lista_completa[contador].append([])
    lista_completa[contador].append([])
    nome = str(input("Nome >: "))
    lista_completa[contador][0].append(nome)
    nota1 = float(input("Nota 1 >: "))
    lista_completa[contador][1].append(nota1)
    nota2 = float(input("Nota 2 >: "))
    lista_completa[contador][1].append(nota2)
    lista_completa[contador].append([(nota1+nota2)/2])
    while continuar not in "SsNn":
        continuar = str(input("Quer cadastrar outro aluno?[S/N] >: "))
    if continuar in "Nn":
        break
    continuar = " "
    contador += 1
print(lista_completa)
