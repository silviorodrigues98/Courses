"""
CRIAR PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA,
QUE RECEBA AS DIMENSÕES DO TERRENO E MOSTRE SUA ÁREA.

"""


def area():
    largura = float(input("Qual a largura do terreno, em METROS? .> "))
    comprimento = float(input("E qual o comprimento, também em METROS? .> "))
    area_total = largura*comprimento
    print(f"A área de um terreno {largura:.1f} x {comprimento:.1f} é de {area_total:.1f}m². ")


area()
