expre = str(input("Digite a expressão: >> ")).strip()
parenteses_aberto = list()
parenteses_fechado = list()
contador = 0
if expre.index("(") >= 0:
    for cont, cada in enumerate(expre):
        if cada in "(":
            parenteses_aberto.append(cont)
        if cada in ")":
            parenteses_fechado.append(cont)
    for conta, teste in enumerate(range(0, len(parenteses_fechado))):
        if len(parenteses_fechado) == len(parenteses_aberto):
            if parenteses_fechado[conta] > parenteses_aberto[conta]:
                contador += 1
    if contador == len(parenteses_aberto):
        print("Esta é uma expressão válida. Parabéns!")
    else:
        print("Esta expressão é inválida! Tente novamente.")
