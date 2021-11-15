""" TUPLA COM VÁRIAS PALAVRAS.
SEM USAR ACÊNTOS.
MOSTRAR PARA CADA PALAVRAS, QUAIS SÃO SUAS VOGAIS. """

palavras = ("PROGRAMACAO", "LIBERTARIANISMO", "ANARQUISMO", "LIVREMERCADO",
            "FUNDOS IMOBILIARIOS", "FOREX", "ELETRONICA",
            "PORNOGRAFIA", "CRIPTOMOEDAS", "BITCOIN", "ETHERIUM", "STOCKS", "RAYNISMO", "AGORISMO", "INDIVIDUALISMO",
            "CAPITALISMO MALVADAO", "KATRINA JADE")
vogais = "A", "E", "I", "O", "U"
vogals = words = 0
while words < len(palavras):
    print(f"Na palavra ; {palavras[words]}, temos:")
    for contador in range(0, 5):
        print(f"{palavras[words].count(vogais[vogals])} letras > {vogais[vogals]} /// ", end=" " if contador < 4 else print(end=""))
        vogals += 1
    print('-='*45)
    words += 1
    vogals = 0
print(f"\n{'OBRIGADO POR USAR NOSSO VOGALIZADOR. VOLTE LOGO !':^80}")
