def leiaint(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem))
        except:
            print(f"""\033[0;31mERRO! O usuário não digitou um número inteiro.
Tente novamente.\033[m""")
        else:
            break
    return inteiro


def leiafloat(mensagem):
    while True:
        try:
            real = float(input(mensagem))
        except:
            print(f"""\033[0;31mERRO! O usuário não digitou um valor real.
Tente novamente.\033[m""")
        else:
            break
    return real
