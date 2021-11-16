valores = []
while True:
    valores.append(input("Digite um valor > "))
    resp = str(input("Quer continuar?[S/N] > "))
    if resp in "Nn":
        break
print("-="*30)
print(f"Você digitou {len(valores)} números")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {valores}")
if 5 in valores:
    print("O número 5 está sim na lista.")
else:
    print("O valor 5 não foi encontrado.")
