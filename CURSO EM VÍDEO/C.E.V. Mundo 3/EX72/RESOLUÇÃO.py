cont = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE",
        "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
while True:
    num = int(input('Digite um valor entre 0 e 20  > '))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ")
print(f"Você digitou o número {cont[num]}")