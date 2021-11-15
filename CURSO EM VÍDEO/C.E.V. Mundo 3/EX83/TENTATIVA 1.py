""" CRIAR PROGRAMA QUE VÊ SE A EXPRESSÃO MATEMÁTICA É CORRETA. """
exp = str(input("Digite sua empressão matematica: >>> "))
if exp.count("(") == exp.count(")") and exp.count("()") == 0:
    print("Válida!")
else:
    print("Inválida!")

