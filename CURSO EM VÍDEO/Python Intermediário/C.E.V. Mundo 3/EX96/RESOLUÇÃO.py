def área(largura, comprimento):
    a = largura * comprimento
    print(f"A área de um terreno de {largura} x {comprimento} é de {a}m².")


print("  CONTROLE DE TERRENOS ")
print("-"*30)
l = float(input("Largura(m): "))
c = float(input("Comprimento(m): "))
área(l, c)
