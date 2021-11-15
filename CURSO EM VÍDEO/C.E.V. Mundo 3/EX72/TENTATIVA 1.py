""" CRIAR UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA, QUE CONTE DE 0 ATÉ 20.
E MOSTRE O VALOR POR EXTENSO. """

numeros_extenso = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE",
                   "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
numero_usuario = 21
continuar = " "
while numero_usuario > 20:
    numero_usuario = int(input('Digite um número > '))
    if 0 <= numero_usuario <= 20:
        print(f"Você digitou o número {numeros_extenso[numero_usuario]}")
        while continuar not in "SsNn":
            continuar = str(input('Você deseja continuar?[S/N] > ')).strip().upper()[0]
        if continuar in "Nn":
            break
    else:
        print("Opção inválida! Digite um número de 0 a 20. ")
    numero_usuario = 21
    continuar = " "
print('CALCULADORA FINALIZADA. ATÉ LOGO!')
