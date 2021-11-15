"""print(input.__doc__)
help(input)  # São as mesmas.
"""


"""def contador(i, f, p):  # Serve para explicar suas funções para quem é "de fora"."""
"""  # Deve se usar 3 aspas duplas embaixo do comando def, para poder criar um manual personalizado. #
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    Função criada por Silvio Correa.
    """
"""    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("FIM")


contador(2, 10, 2)
help(contador)
#  help(random)


def somar(a=0, b=0, c=0):  # Este valor 0 depois do C faz com que ele receba 0 caso não haja valor informado.
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 2, 5)
somar(3, 2)
somar(3)
somar(c=4, b=2)  # Isto inverte a ordem de forma forçada"""

"""
def teste(num):
    a = 8  # x tem scopo local, pois só funciona aqui dentro do DEF.
    b = num+7
    c = num-2
    print(f"A Na função teste,  vale {a}")


a = 2
print(f"A No programa pincipal, o A vale {a}")  # No python, ele cria uma variável repetida dentro do DEF,
# mas ele não é modificada pelas alterações.
teste(a)"""
#  X não existe aqui fora da DEF.

#  Vale lembrar que, além disso, também existem exportaçoes locais,
#  onde um módulo é exportado somente dentro de um escopo.


"""def teste1(num):
    global a  # Isto faz com que o A dentro do DEF se torne global e, assim,
    # altere as modificações do A que está fora.
    a = 8  # x tem scopo local, pois só funciona aqui dentro do DEF.
    b = num+7
    c = num-2
    print(f"A Na função teste,  vale {a}")


a = 2
teste1(a)
print(f"A No programa pincipal, o A vale {a}")
"""


"""def somar(a=0, b=0, c=0):
    s = a+b+c
    return s  # Faz com o que o valor S seja passado para uma variável exterior, no caso "resp"


r1 = somar(3, 2, 5)
r2 = somar(2, 4)
r3 = somar(4)
print(f"Os valores somados foram {r1}, {r2}, {r3}")
"""


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual à {fatorial(n)}")

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"As fatoriais digitadas foram {f1}, {f2}, {f3}.")


def par(n=0):
    if n % 2 == 0:
        return True  # É possível retornar quaisquer tipos de valores, como boleanos e listas, etc.
    else:
        return False


num = int(input("Digite um número; "))
if par(num):
    print("É par.")
else:
    print("Não é par.")
