valores = list()
continuar = " "
contador = 0
while True:
    num = int(input('Digite um valor: > '))
    valores.append(num)
    contador += 1
    while continuar not in "SsNn":
        continuar = str(input('Deseja adicionar outro?[S/N] > ')).upper().strip()[0]
    if continuar in "Nn":
        break
    continuar = " "
valores.sort(reverse=True)
print(f"Foram digitados {contador} valores.")
print(f"São eles : {valores}")
if valores.count(5) > 0:
    print("O valor 5 está sim na lista.")
else:
    print("O valor 5 não está na lista.")
