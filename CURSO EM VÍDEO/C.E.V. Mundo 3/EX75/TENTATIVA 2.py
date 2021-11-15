v1 = v2 = v3 = v4 = teste_pares = 0
for valores in range(0, 4):
    valor = int(input("Digite um valor > "))
    if valores == 0:
        v1 = valor
    elif valores == 1:
        v2 = valor
    elif valores == 2:
        v3 = valor
    else:
        v4 = valor
valores = v1, v2, v3, v4
print(valores)
if 9 in valores:
    print(f"O número 9 apareceu {valores.count(9)} vezes.")
else:
    print("O valor 9 não foi digitado em nenhuma posição ")
if 3 in valores:
    print(f"O número 3 se encontra na {valores.index(3)+1}ª posição.")
else:
    print('O número 3 não foi digitado em nenhuma posição ')
print(f"Dos quatro números, foram pares: ", end=' ')
for teste_pares in range(0, 4):
    if valores[teste_pares] % 2 == 0:
        print(valores[teste_pares], end="...")
print("FIM" if teste_pares == 3 else print())

