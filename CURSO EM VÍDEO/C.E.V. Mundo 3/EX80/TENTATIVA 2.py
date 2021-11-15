valores = list()
for val in range(0, 5):
    v = int(input("Digite um número > "))
    if val == 0:
        valores.append(v)
        print("Valor adicionado na última posição...")
        maior = v
        menor = v
        medio = v
    else:
        if v >= maior:
            maior = v
            print("Valor tomou o lugar na última posição")
            valores.append(v)
        if v <= menor:
            menor = v
            print("Valor adicionado na posição 0...")
            valores.insert(0, v)
        if maior > v > menor:
            print("O valor foi adicionado à 1ª posição...")
            medio = v
            valores.insert(1, v)
print(f"Você digitou os valores, em ordem crescente: {valores}")
