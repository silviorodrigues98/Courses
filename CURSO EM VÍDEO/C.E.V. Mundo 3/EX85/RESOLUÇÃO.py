num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input("Digite um valor >: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("-="*30)
num[1].sort()
num[0].sort()
print(f"Os valores pares foram: {num[0]}")
print(f"Os valores impares foaram: {num[1]}")