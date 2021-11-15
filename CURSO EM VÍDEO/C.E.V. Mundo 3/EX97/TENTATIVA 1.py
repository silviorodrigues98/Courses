"""
CRIAR FUNÇÃO CHAMADA ESCREVA, QUE RECEBA UM TEXTO QUALQUER,
E MOSTRE UMA MENSAGEM DE TAMANHO ADAPTÁVEL.

"""


def escreva(*msg):
    msg = str(input("Olá ! Qual mensagem você quer escrever hoje? .> ")).strip()
    print("~"*(len(msg)+4))
    print(f"  {msg}")
    print("~"*(len(msg)+4))


escreva()
