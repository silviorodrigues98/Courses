barato = ' '
total = totmil = menor = cont = 0
while True:
    produto = str(input('Nome do produto > '))
    preco = float(input('Preco do produto >R$ '))
    total += preco
    cont += 1
    if preco > 100:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] > ')).strip().upper()[0]
    if resp == 'N':
        break
print(f"{'FIM DO PROGRAMA':-^40}")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de mil reais.")
print(f"O produto mais barato é {barato} e custa {menor:.2f}")
