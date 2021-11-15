c = ("\033[m",          # 0 -  SEM CORES
     "\033[0;30;41",    # 1 - VERMELHO
     "\033[0;30;42m",   # 2 - VERDE
     "\033[0;30;43m",   # 3 - AMARELO
     "\033[0;30;44m",   # 4 - AZUL
     "\033[0;30;45m",   # 5 - ROXO
     "\033[0;30;46m"    # 6 - BRANCO
     )


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0])


#  PROGRAMA PRINCIPAL:


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP")
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO", 3)
