temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input(f"nome >: ")))
    temp.append(float(input(f"peso >: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Continuar? >: "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Os dados foram {princ}")
print(F"Ao todo você cadastrou {len(princ)}")
print(f"o maior foi {maior}, peso de: ",end="")
for p in princ:
    if p[1] == maior:
        print(f"{p[0]} ", end="")
print()
print(f"O menor foi {menor} peso de: ", end="")
for p in princ:
    if p[1] == menor:
        print(p[0])
