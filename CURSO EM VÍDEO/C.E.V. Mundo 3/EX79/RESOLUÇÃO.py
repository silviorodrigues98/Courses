numeros = []
while True:
    n = int(input("Digite um valor > "))
    if n not in numeros:
        print("Valor adicionado.")
        numeros.append(n)
    else:
        print("Valor duplicado.")
    r = str(input("Continuar[S/N] > "))
    if r in "Nn":
        break
print("-="*30)
numeros.sort()
print(f"Você digitou os valores: {numeros}")
