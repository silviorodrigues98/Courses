listagem = ("LÁPIS", 1.75,
            "BORRACHA", 2,
            "CADERNO,", 15.90,
            "ESTOJO", 25,
            "TRANSFERIDOR", 4.20,
            "MOCHILA", 120.32,
            "LIVRO", 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end=" ")
    else:
        print(f"R$ {pos:>5.2f}")
