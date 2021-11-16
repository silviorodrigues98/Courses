"""PROGRAMA QUE LÊ PREÇOS E PRODUTOS, E DA INFORMAÇÕES SOBRE ELES, USANDO WHILE. """
from time import sleep
from emoji import emojize
from playsound import playsound
cores = ['\033[1;3;4;30;46m', "\033[m"]
print(f"""{cores[0]}BEM VINDO À NOSSA LOJA VIRTUAL,
PARA CADASTRAR SUAS COMPRAS
SIGA OS PASSOS A SEGUIR:\n{cores[1]}""")
total_compra = 0
preco_mais_caro = 0
produto_mais_caro = ''
preco_mais_barato = 10**999
produto_mais_barato = ''
cont = 1
maiores_de_1000 = 0
while True:
    produto = str(input(emojize('Qual o nome do produto que você comprou? :smile: > ', use_aliases=True))).upper().strip()
    preco = float(input(emojize('E qual o preço deste produto? :imp: >R$ ', use_aliases=True)))
    total_compra += preco
    if preco >= preco_mais_caro:
        produto_mais_caro = produto
        preco_mais_caro = preco
    if preco <= preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = produto
    if preco >= 1000:
        maiores_de_1000 += 1
    continuar = 'AAA'
    print('Cadastrado com sucesso!')
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar?[S/N] > ')).upper().strip()[0]
    if continuar in "Nn":
        break
print(f"{'Calculando...':^30}"), sleep(1.5)
print(f"""O valor total de sua compra foi de : R${total_compra:.2f}
Sendo que o produto mais caro foi o {produto_mais_caro},no preço de : R${preco_mais_caro:.2f}
Houveram {maiores_de_1000} produtos com preço acima dos R$1.000,00 
Já o produto mais barato foi no preço de : R${preco_mais_barato:.2f},
sendo assim, o(a) {produto_mais_barato}""")
playsound('C:/door.mp3')
