from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: > '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? > ')).upper().strip()[0]
    print(f"Voce jogou {jogador} e o pc {computador}. Total de {total}")
    print('DEU PAR ' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu! ')
            v += 1
        else:
            print('Você perdeu! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! ')
            v += 1
        else:
            print('Você perdeu! ')
            break
print(f'GAME OVER, você venceu {v} vezes seguidas ')
