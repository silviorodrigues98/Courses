""" LISTAS SÃO MODIFICÁVEIS. """


num = [2, 5, 9, 1]
num[2] = 3  # Altera o 9 para 3.
num.append(7)  # Adiciona número 7 no final da lista.
num.sort()  # Organina a lista.
num.sort(reverse=True)  # Organiza em ordem decrescente.
num.insert(2, 0)  # Insere o 0 na posição 2
num.pop()  # Remove último ítem da lista.
num.pop(2)  # Remove o ítem da segunda posição.
num.remove(7)  # Remove o número 7 da lista. "SOMENTE A PRIMEIRA OCORRÊNCIA"
print(num)
print(f"Essa lista tem {len(num)} elementos. ")

valores = list()  # ou valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for posicao, valor in enumerate(valores):  # O Enumerate faz com que o for retorne cada uma de suas repetições.
    print(f"Na posição {posicao+1}, encontrei o valor {valor}...")
numeros = list()
for cont in range(0, 2):
    numeros.append(int(input("Digite um valor > ")))  # Isso adiciona inputs em listas.
print(numeros)

a = [2, 3, 4, 7]
b = a
b[2] = 8  # O comando de alterar B altera também o A, pois eles estão ligados.
print(f"Lista a {a}")
print(f"Lista b {b}")
b = a[:]  # Dessa forma, o B se torna uma cópia de A, e não é alterado.
b[3] = 9
print(f"A >{a} e B >{b}")
