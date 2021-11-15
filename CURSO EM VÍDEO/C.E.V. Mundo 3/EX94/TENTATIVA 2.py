""" PROGRAMA QUE LE NOME SEXO E IDADE DE VÁRIAS PESSOAS, E GUARDA TAIS
DADOS EM UM DICIONÁRIO.
MOSTRAR ALGUMAS INFORMAÇÕES SOBRE ELE. """

cadastro = []
while True:
    pessoa = {"NOME": str(input("Nome >: ")),
            "SEXO": str(input("Sexo[M/F] >; ")).upper().strip()[0],
            "IDADE": int(input("Idade >: "))}
    cadastro.append(pessoa)
    continuar = " "
    while continuar not in "NnSs":
        continuar = str(input("Continuar?[S/N] >: ")).upper().strip()[0]
        if continuar not in "NnSs":
            print("Opção inválida. Digite somente SIM ou NÃO")
    if continuar in "Nn":
        break
idades = 0
mulheres = []
for quantas, cada_uma in enumerate(cadastro):
    for keys, values in cada_uma.items():
        if keys in "NOME":
            nome = values
        if values == "F":
            mulheres.append(nome)
        if keys == "IDADE":
            idades += values
print(f"Foram cadastradas {quantas+1} pessoas.")
print(f"As mulhares que foram cadastradas são : {mulheres}" if len(mulheres) > 0 else "Não foram cadastradas mulheres.")
media = idades/(quantas + 1)
acima_da_media = []
print(f"A média de idade é de {media:.2f} anos. ")
print("Lista de pessoas acima da média: ")
for cada_uma in cadastro:
    for keys, values in cada_uma.items():
        if keys == "IDADE" and values > media:
            print(f"\nnome = {cada_uma['NOME']}; sexo = {cada_uma['SEXO']}; idade = {cada_uma['IDADE']}")
print(" <<< ENCERRADO >>> ")
