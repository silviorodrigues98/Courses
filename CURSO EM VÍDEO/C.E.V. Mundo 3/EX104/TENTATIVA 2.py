"""
FUNÇÃO LEIAINT FUNCIONA COMO INPUT, MAS SÓ ACEITARÁ VALOR NUMÉRICO.

"""


def leiaint(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            break
        else:
            print(f"\033[1;31mERRO! Digite um número inteiro válido.\033[m")
    return int(num)


n = leiaint("Digite um valor :> ")
print(f"Você digitou o número {n}")
