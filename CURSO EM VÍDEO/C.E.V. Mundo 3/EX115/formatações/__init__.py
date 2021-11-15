def cores():
    """
    Cria uma lista com as cores
    :return: retorna esta lista.
    """
    colors = {"vermelho": "\033[0;31m", "verde": "\033[0;32m", "amarelo": "\033[0;33m",
              "azul": "\033[0;34m", "roxo": "\033[0;35m",
              "marinho": "\033[0;36m", "cinza": "\033[0;37m", "vazio": "\033[m"}
    return colors


def print_cores(frase="", cor="vazio"):
    """
    Pega uma frase a printa formatada com as cores,
    :param frase:frase a ser formatada
    :param cor:cor desejada (em string)
    :return:printa a frase já colorida.
    """
    colorir = cores()
    print(f"{colorir[cor]}{frase}{colorir['vazio']}")


def linhas(tipo="-", tamanho=30):
    """
    Printa linhas formatadas personalizaveis.
    :param tipo:qual forma à ser printada
    :param tamanho:tamanho multiplicador da linha
    :return:printa a linha personalizada
    """
    print(tipo * tamanho)


def print_linhas(frase="", tipo="-", tamanho=30, ajustar=False):
    """
    Printa a frase em meio à linhas personalizaveis
    :param frase: frase a ser printada
    :param tipo: figura da linha
    :param tamanho: tamanho multiplicador da linha
    :param ajustar: Booleano, se verdadeiro, faz com que a
    linha se ajuste de acordo com a frase
    :return: printa a frase formatada entre linhas.
    """
    if ajustar:
        tamanho = len(frase) + 4
    print(tipo * tamanho)
    print(f"{frase:^{tamanho}}")
    print(tipo * tamanho)
