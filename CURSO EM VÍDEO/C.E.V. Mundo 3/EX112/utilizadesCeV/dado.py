def leiaDinheiro(txt):
    while True:
        valor = str(input(txt))
        if valor in "," or ".":
            valor = valor.replace(",", ".").split(".")
            if valor[0].isnumeric() and valor[1].isnumeric():
                valor = float(valor[1])/(10**len(valor[1])) + int(valor[0])
                break
        else:
            if valor.isnumeric():
                valor = int(valor)
                break
        print("\033[31mERRO! Digite um valor monetário.\033[m ")
    return valor
