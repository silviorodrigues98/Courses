from random import randint as rdt
var = (rdt(0, 10), rdt(0, 10), rdt(0, 10), rdt(0, 10), rdt(0, 10))
print(f"Sorteei os valores {var}")
for num in var:
    print(num, end=" -> ")
print(f"\nO maior valor sorteado foi {max(var)}")
print(f"O menor valor sorteado foi {min(var)}")
