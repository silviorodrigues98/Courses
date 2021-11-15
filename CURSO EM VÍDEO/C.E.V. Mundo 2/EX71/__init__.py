from time import sleep
from emoji import emojize
from playsound import playsound as pl

cores = ['\033[1;3;4;30;43m', "\033[m"]
emojis = [':sunglasses:', ':smile:', ':imp:']
print(f"{cores[0]}BANCO LIBERTÁRIO{cores[1]}")
cedula_1 = cedula_10 = cedula_20 = cedula_50 = resto = 0
valor_do_saque = int(input(emojize('Quanto você deseja sacar? :smile: >R$ ', use_aliases=True)))
print(f'Seu saque é de R${valor_do_saque:.2f}:')
print(f"{'Calculando...':^30}"), sleep(1.5)
if valor_do_saque >= 50:
    cedula_50 = valor_do_saque // 50
    resto = valor_do_saque % 50
    print(emojize(f"{emojis[0]}Você vai receber {cedula_50} cédulas de R$50,00", use_aliases=True))
else:
    resto = valor_do_saque
if resto >= 20:
    cedula_20 = resto // 20
    resto %= 20
    print(emojize(f"{emojis[1]}Você vai receber {cedula_20} cédulas de R$20,00", use_aliases=True))
if resto >= 10:
    cedula_10 = resto // 10
    resto %= 10
    print(emojize(f"{emojis[2]}Você vai receber {cedula_10} cédulas de R$10,00", use_aliases=True))
cedula_1 = resto
if resto >= 1:
    print(emojize(f"{emojis[1]}VocÊ vai receber {cedula_1} cédulas de R$1,00", use_aliases=True))
print(f"\n{cores[0]}OBRIGADO POR USAR NOSSOS SERVIÇOS, ATÉ LOGO!\n{cores[1]}")
pl('C:/door.mp3')
