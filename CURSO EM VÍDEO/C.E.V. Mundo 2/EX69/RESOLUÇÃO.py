tot18 = toth = totm20 = 0
while True:
    idade = int(input('Cadastre a idade: > '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Caadastre o sexo: > ")).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar [S/N] > ')).upper().strip()[0]
    if resp == 'N':
        break
print(f"Total de pessoas com mais de 18 anos : {tot18}")
print(f"Ao todo temos {toth} de homens cadastrados")
print(f"E temos {totm20} mulheres com menos de 20 anos.")
