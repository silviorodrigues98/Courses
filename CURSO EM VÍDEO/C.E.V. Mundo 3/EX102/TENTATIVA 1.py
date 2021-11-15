"""
FUNÇÃO FATORIAL QUE RECEBE DOIS PARAMETROS.
O PRIMEIRO INDICA O NÚMERO E O OUTRO MOSTRA UM VALOR LÓGICO(OPCIONAL)
INDICANDO SE SERÁ MOSTRADO OU NÃO O PROCESSO DE CÁLCULO NA TELA.

"""


def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.
    :param numero: número a ser calculado
    :param show: Mostra ou não a conta
    :return: retorna o resultado.
    """
    multiplicacoes = 1
    for resultado in range(numero, 0, -1):
        multiplicacoes *= resultado
        if show:
            if resultado > 1:
                print(f"{resultado} x", end=" ")
            else:
                print(resultado, "=", end=" ")
    return multiplicacoes


fat = int(input("Qual o número que você quer a fatorial? "))
mostrar = " "
while mostrar not in "SsNn":
    mostrar = str(input("Deseja mostrar o cálculo?[S/N] ")).upper().strip()[0]
if mostrar in "Ss":
    mostrar = True
else:
    mostrar = False
print(fatorial(fat, mostrar))
