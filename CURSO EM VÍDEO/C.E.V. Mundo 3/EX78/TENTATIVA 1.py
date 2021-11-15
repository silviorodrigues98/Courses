""" programa que leia 5 valores numéricos e os guarde em uma lista.
 No final, mostre o maior valor e o menor, além de suas respectivas posições na lista."""

valores = list()
for contador, valor in enumerate(range(0, 5)):
    valores.append(int(input(f"Digite o {contador+1}º valor > ")))
maior = max(valores)
menor = min(valores)
posmaior = list()
posmenor = list()
for count, posicao in enumerate(valores):
    if valores[count] == maior:
        posmaior.append(count+1)
    if valores[count] == menor:
        posmenor.append(count+1)
print(f"O maior valor foi {maior} e se encontra nas posições: {posmaior}")
print(f"O menor valor foi {menor} e se encontra nas posições: {posmenor}")
