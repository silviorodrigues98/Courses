valores = list()
maior = 0
menor = 0
medio = 0
for val in range(0, 5):
    v = int(input("Digite um número > "))
    if val == 0:
        valores.append(v)
        maior = v
        menor = v
        medio = 0
        print("Valor adicionado na última posição...")
    else:
        if v >= maior:
            maior = v
            print("Valor tomou o lugar na última posição")
            valores.append(v)
        if v <= menor:
            menor = v
            print("Valor adicionado na posição 0...")
            valores.insert(0, v)
        if val == 2:
            if maior > v > menor:
                print("O valor foi adicionado à 1ª posição...")
                valores.insert(1, v)
        if val == 3:
            if maior > v > valores[1]:
                valores.insert(2, v)
                print("O valor foi adicionado à 2ª posição")
            if menor < v < valores[1]:
                valores.insert(1, v)
                print("O valor foi adicionado à 1ª posição")
        if val == 4:
            if valores[2] > v > valores[1]:
                valores.insert(2, v)
                print("O valor foi adicionado à 2ª posição")
            if maior > v > valores[2]:
                valores.insert(3, v)
                print("O valor foi adicionado à 3ª posição")
            if menor < v < valores[1]:
                valores.insert(1, v)
            print("Você inseriu o último valor!")
print(f"Você digitou os valores, em ordem crescente: {valores}")
