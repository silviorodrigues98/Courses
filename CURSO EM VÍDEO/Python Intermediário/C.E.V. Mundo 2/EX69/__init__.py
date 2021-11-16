""" LEIA IDADE E SEXO DE VÁRIAS PESSOAS E PERGUNTAR SE QUER CONTINUAR OU NÃO
 APÓS ISSO, DAR ALGUMAS INFORMAÇÕES """
from time import sleep
from emoji import emojize
from playsound import playsound
cores = ['\033[1;3;4;30;44m', '\033[m']
print(f"""{cores[0]}BEM VINDO AO NOSSO SISTEMA DE CADASTROS!
CADASTRE NOSSOS CLIENTES QUANTAS VEZES FOR NECESSÁRIO, BASTA SEGUIR AS INSTRÇÕES: \n{cores[1]}""")
contador_pessoas_18 = 0
contador_homens = 0
contador_mulheres_20 = 0
while True:
    idade = int(input(emojize('Digite a idade :sunglasses: > ', use_aliases=True)))
    if idade >= 18:
        contador_pessoas_18 += 1
    sexo = 'AAA'
    while sexo not in 'MmFf':
        sexo = str(input(emojize("Digite o sexo [M/F] :smile: >  ", use_aliases=True))).upper().strip()[0]
    print('Cadastrado com sucesso! ')
    if sexo in 'M':
        contador_homens += 1
    if sexo in 'F' and idade < 20:
        contador_mulheres_20 += 1
    continuar = 'AAA'
    while continuar not in 'SsNn':
        continuar = str(input(emojize('Quer continuar? [S/N] :imp: > ', use_aliases=True))).strip().upper()[0]
    if continuar in 'N':
        break
print('Salvando...'), sleep(1.5)
print(f'''{cores[0]}Foram cadastradas {contador_pessoas_18} pessoas maiores de 18 anos.
De todos cadastrados. {contador_homens} eram homens.
Além disso, {contador_mulheres_20} mulheres com menos de 20 anos foram cadastradas hoje.\n{cores[1]}''')
playsound('C:/door.mp3')
