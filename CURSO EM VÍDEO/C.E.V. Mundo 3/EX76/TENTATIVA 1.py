""" TUPLA ÚNICA COM NOMES DOS PRODUTOS, RESPCTIVOS PREÇOS NA SEQUÊNCIA. """


produtos_e_valores = ("PÃO", 0.50, "LEITE", 3, "MANTEIGA", 5, "ARROZ", 12, "FEIJÃO", 10,
                      "AÇUCAR", 6, "MACONHA", 20, "CARNE", 30, "FARINHA", 12)
produto = 0
preco = 1
print('='*60)
print(f"{'LISTA DE PREÇOS':^60}")
print('='*60)
for listagem in range(0, len(produtos_e_valores)-9):
    print(f"{produtos_e_valores[produto]:.<50}, R$ {produtos_e_valores[preco]:<50.2f}")
    produto += 2
    preco += 2
print('='*60)
