def leiaDinheiro(txt):
    while True:
        valor = str(input(txt))
        if valor in "," or ".":
            valor = valor.replace(",", ".").split(".")
            if valor[0].isnumeric() and valor[1].isnumeric():
                valor1 = int(valor[0])
                valor2 = float(valor[1])/(10**len(valor[1]))
                valor3 = float(valor1+valor2)
                break
        else:
            if valor.isnumeric():
                valor3 = int(valor)
                break
        print("\033[31mERRO! Digite um valor monetário.\033[m ")

    return valor3
