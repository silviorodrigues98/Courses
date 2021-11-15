from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print("-="*20)
        print(f"Contagem de {i} até o {f}, de {p} em {p}")
        sleep(2)
        cont = i
        while cont <= f:
            print(f"{cont} ", end=" ", flush=True), sleep(0.5)
            cont += p
        print("FIM")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end=" ", flush=True), sleep(0.5)
            cont -= p
        print("FIM")


contador(1, 10, 1)
contador(10, 0, 2)
print("-="*20)
print("Agora é sua vez de personalizar sua contagem: ")
ini = int(input("Inicio: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))
contador(ini, fim, pas)
