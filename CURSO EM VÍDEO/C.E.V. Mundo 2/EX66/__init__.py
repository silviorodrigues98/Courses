''' PROGRAMA QUE LE NUMEROS INTEIROS, E SÓ PARA QUANDO O USUÁRIO DIGITAR O VALOR 999, NO FINAL MOSTRE '''
from time import sleep
from emoji import emojize
from playsound import playsound
print('SEJA MUITO BEM VINDO À SUA SOMA++FÁCIL, A SUA CALCULADORA INTELIGENTE!')
print("\033[1;3;4;30;42m-=\033[m" * 40)
quantidade_vezes = 1
soma_numeros = 0
while True:
    numero = int(input(emojize(f'Diga seu {quantidade_vezes}º número::smile:[999 p/ sair] ',use_aliases=True)))
    print('...'), sleep(0.25)
    if numero == 999:
        break
    quantidade_vezes += 1
    soma_numeros += numero
quantidade_vezes -= 1
print(f"Você digitou {quantidade_vezes} números e a soma entre eles é : {soma_numeros}")
playsound("C:/door.mp3")

