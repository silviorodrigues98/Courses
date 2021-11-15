"""
PROGRAMA QUE UTILIZA O INTERACTIVE HELP ATRAVÉS DOS COMANDOS, COMO SE FOSSE UM CONSOLE.

"""
from time import sleep


def titulos(cor="", txt="", fim="\033[m"):
    print(cor, end="")
    print("~" * (len(txt)+4))
    print(f"  {txt}")
    print("~" * (len(txt)+4))
    print(fim)


cores = {"vr": "\033[1;41m", "vd": "\033[1;30;42m",
         "am": "\033[1;43m", "az": "\033[1;30;44m",
         "rx": "\033[1;45m", "mr": "\033[1;30;46m",
         "ci": "\033[1;47m", "fn": "\033[m"}

while True:
    titulos(cores['vd'], "SISTEMA DE AJUDA PyHELP"), sleep(1)
    usuario = str(input("Função ou Biblioteca > ")).strip().lower()
    sleep(1)
    if usuario.upper().strip() in "FIM":
        titulos(cores['vr'], "ATÉ LOGO!")
        break
    titulos(cores['az'], f"Acessando o manual do comando {usuario}"), sleep(1)
    print(f"{cores['ci']}")
    help(usuario)
    print(f"{cores['fn']}")
