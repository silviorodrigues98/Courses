"""
print("-="*30)
print("CURSO EM VIDEO")
print("-="*30)
print("-="*30)
print("APRENDA PYTHON")
print("-="*30)
print("-="*30)
print("SILVIO CORREA")
print("-="*30)


def lin():
    print("-=" * 30)  # Só executa quando chamada.


print("CURSO EM VIDEO")
lin()
print("APRENDA PYTHON")
lin()
lin()
print("SILVIO CORREA")
lin()


def mensagem(msg):  # Cria uma variável que possibilita usar os parâmetros.
    print("-=" * 30)
    print(msg)
    print("-=" * 30)


mensagem("SISTEMAS DE ALUNOS")


def titulo(txt):
    print("-=" * 30)
    print(txt)
    print("-=" * 30)


titulo("PYTHON É MUITO DAHORA!")
"""

"""
a = 5
b = 5
s = a+b
print(s)
a = 8
b = 9
s = a+b
print(s)
a = 2
b = 1
s = a+b
print(s)
"""


def soma(a, b):  # Faz o mesmo processo anterior de forma mais fácil
    print(f"A = {a} B = {b}")
    s = a+b
    print(f"A soma vale {s}")


soma(b=4, a=5)  # Isso muda a ordem dos parâmetros.
soma(8, 9)
soma(2, 1)


"""def contador(*num):  # O asterisco cria uma tupla com os valores, quando a qtde é indefinida.
    for valor in num:
        print(f"{valor} ", end="")
    print("FIM")"""


def contador(*num):  # O asterisco cria uma tupla com os valores, quando a qtde é indefinida.
   tam = len(num)
   print(f"Recebi os valores {num} e são ao todo {tam} números.")


contador(7, 2, 4)
contador(8, 0)
contador(1, 5, 6, 2)


valores = [2, 5, 8, 9, 4]


def dobra(lst):  # Tudo que acontecer aqui influencia a lista abaixo.
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


dobra(valores)
print(valores)


def soma(*nums):
    s = 0
    for num in nums:
        s += num
    print(f"Somando os valores {nums} temos: {s}")


soma(5, 2)
soma(2, 9, 10, 89)
