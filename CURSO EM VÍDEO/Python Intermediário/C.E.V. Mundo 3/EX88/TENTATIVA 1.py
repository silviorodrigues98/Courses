"""PALPITES DA MEGA SENA! """
from random import randint
from time import sleep


todos_jogos = []
random = 0
print("-="*20, f"""
{'JOGA NA MEGA SENA':^40}
""", "-="*20)
qtde = int(input("Quantos jogos você quer? >: "))
inicio = f"SORTEANDO {qtde} JOGOS"
print(f"{inicio:=^40}")
for contador, jogos in enumerate(range(0, qtde)):
    todos_jogos.append([])
    for numeros in range(0, 6):
        random = randint(1, 60)
        if todos_jogos[contador].count(random) == 0:
            todos_jogos[jogos].append(random)
        else:
            random = randint(0, 60)
            todos_jogos[jogos].append(random)
    todos_jogos[contador].sort()
    print(f"Jogo {jogos+1}: {todos_jogos[jogos]}"), sleep(1)
print(f"{' BOA SORTE! ':=^40}")
