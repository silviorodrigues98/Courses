palavras = ("PROGRAMACAO", "LIBERTARIANISMO", "ANARQUISMO", "LIVREMERCADO",
            "FUNDOS IMOBILIARIOS", "FOREX", "ELETRONICA",
            "CRIPTOMOEDAS", "BITCOIN", "ETHERIUM", "STOCKS", "RAYNISMO", "AGORISMO", "INDIVIDUALISMO",
            "CAPITALISMO MALVADAO", "KATRINA JADE")
for p in palavras:
    print(f"\nNa palavra {p} temos:", end="")
    for letra in p:
        if letra.upper() in "AEIOU":
            print(letra, ",", end="")
