"""TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR.
SERÁ INTERROMPIDO QUANDO O USUÁRIO DIGITAR NÚMERO NEGATIVO. """
from time import sleep
from emoji import emojize
from playsound import playsound

lista = ['\033[1;3;4;30;41m', '\033[m']
print(f"""{lista[0]}BEM VINDO AO TABUADOR!!!
BASTA DIGITAR UM NÚMERO E SABERÁ SUA TABUADA !!!\n{lista[1]}""")
contador = 1
while True:
    valor = int(input(emojize('Quer ver a tabuada de qual valor?:imp: ', use_aliases=True)))
    if valor < 0:
        break
    while contador < 11:
        total = valor * contador
        print(f"{'Calculando...':^20}"), sleep(1)
        print(f"{valor} x {contador} = {total}")
        contador += 1
    else:
        contador = 1
print(f'\n{lista[0]}PROGRAMA ENCERRADO COM SUCESSO. ATÉ LOGO !\n{lista[1]}')
playsound("C:/door.mp3")
