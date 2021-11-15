num = []
while True:
    num.append(int(input("Digite um valor > ")))
    resp = str(input("Quer continuar? > "))
    if resp in "Nn":
        break
pares = []
impares = []
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print("-="*30)
print(f"A lista completa é: {num}")
print(f"A lista de pares é: {pares}")
print(f"A lista de ímpares é: {impares}")
