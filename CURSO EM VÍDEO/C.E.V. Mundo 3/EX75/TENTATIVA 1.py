""" PROGRAMA QUE LÊ 4 NÚMEROS E DIZ ALGUMAS INFORMAÇÕES SOBRE ELES.
TODOS DEVEM FICAR GUARDADOS EM UMA TUPLA """
cont_pares = teste_pares = 0
valor1 = int(input('Digite o primeiro valor > '))
valor2 = int(input('Digite o segundo valor  > '))
valor3 = int(input("Digite o terceiro valor > "))
valor4 = int(input("Digite o quarto valor > "))
valores = valor1, valor2, valor3, valor4
print(f"VocÊ digitou{valores}")
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
print("FIM" if teste_pares else "")
