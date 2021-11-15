listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c} > ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print("-="*30)
print(f"Você digitou os valores {listanum}")
print(f"O maior valor foi {maior} nas posições: ", end="")
for cont, valor in enumerate(listanum):
    if valor == maior:
        print(f"{cont}...", end="")
print()
print(f"O menor valor foi {menor} nas posições: ", end="")
for cont, valor in enumerate(listanum):
    if valor == menor:
        print(f"{cont}...", end="")
