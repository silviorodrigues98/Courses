galera = []
pessoa = dict()
soma = media = 0
while True:
    pessoa["NOME"] = str(input("Nome: "))
    while True:
        pessoa["SEXO"] = str(input("Sexo: [M/F] ")).upper().strip()[0]
        if pessoa["SEXO"] in "MF":
            break
        print("ERRO! Por favor digite apenas F ou M. ")
    pessoa["IDADE"] = int(input("Idade: "))
    soma += pessoa["IDADE"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Continuar? [S/N] ")).upper().strip()[0]
        if resp in 'SN':
            break
        print("ERRO! Digite apenas S ou N. ")
    if resp == "N":
        break
print("-="*30)
print(galera)
print(f"Ao todo temos {len(galera)} pessoas cadastradas. ")
media = soma/len(galera)
print(f"A média de idade é de {media:5.2f} anos.")
print(f"As mulheres cadastradas foram ", end="")
for p in galera:
    if p["SEXO"] == "F":
        print(f"{p['NOME']} ", end="")
print(f"Lista das pessoas acima da média: ", end="")
for p in galera:
    if p["IDADE"] >= media:
        print("    ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
print("<< ENCERRADO >>")
