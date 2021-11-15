lanche = "hamburguer", "suco", "pizza", "pudim"  # TUPLA USA PARÊNTESES, MAS SÃO É OBRIGATÓRIO.
print(lanche[1])
print(lanche[0])
print(lanche[3:5])
print(lanche[:2])
print(lanche[0:2])  # NÃO PEGA O ÚLTIMO [2]
print(lanche[1:])  # VAI DO SUCO ATÉ O FINAL.
print(lanche[-1])  # PEGA DO ÚLTIMO.
print(lanche[-3])
print(lanche[-2:4])
print(len(lanche))

for comida in lanche:  # PEGA TODOS OS ÍTENS DO LANCHE.
    print(comida, end='...')  # IMPRIME UM DE CADA VEZ.
for almoco in lanche:
    print(f"\nEu vou comer {sorted(almoco)}. Comi pra caramba!")  # ESTE MÉTODO ORDENA OS PRODUTOS.
for cafe in range(0, len(lanche)):
    print(f"\nESTA É OUTRA FORMA DE ESCREVER OS ÍTENS.{lanche[cafe]}")  # OUTRA FORMA DE SE FAZER A MESMA LISTAGEM.
for comida, pos in enumerate(lanche):  # PEGA TODOS OS ÍTENS DO LANCHE.
    print(comida, pos, end='...')  # PARA USAR ENUMERATE, DEVEM HAVER DUAS VARIÁVEIS NO FOR "COMIDA, POS".

numeros1 = (2, 5, 4)
numeros2 = (5, 8, 1, 2)
numerossoma = numeros1 + numeros2  # A SOMA DE TUPLAS NÃO NECESSARIAMENTA AS SOMA, MAS SIM, AS JUNTA EM UMA TUPLA SÓ.
print(numerossoma)

#  TUPLAS SÃO IMUTÁVEIS, OU SEJA, NÃO SE PODE ALTERAR O PRODUTO DA LISTA.
#  lanche[1] = "CAFÉ" # PROVA DE QUE TUPLAS SÃO IMUTÁVEIS.
#  MODIFICADORES -> SORTED, ENUMERATE, LEN

print(len(numerossoma))
print(numerossoma.count(5))  # AS TUPLAS TÊ MFUNÇÕES PRÓPIAS, COMO COUNT. ASSIM, ELE CONTA O NÚMERO DE 5, POR EXEMPLO.
print(numerossoma.index(8))  # RETORNA A POSIÇÃO DO NÚMERO 8 DENTRO DA TUPLA, EM SUA PRIMEIRA OCORRÊNCIA

pessoa = "SILVIO", 39, 80, 1.80  # DIFERENTE DE OUTRAS LINGUAGENS, O PYTHON ACEITA NÚMEROS E STRINGS NA MESMA TUPLA
print(pessoa)
del pessoa
#  print(pessoa)  # A ÚNICA MODIFICAÇÃO POSSÍVEL EM TUPLA É EXCLUÍ-LA, POR ISSO, APOS O COMANDO "DEL",
#  FICA IMPOSSÍVEL PRINTAR A VARIÁVEL "PESSOA"
