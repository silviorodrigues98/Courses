"""
PROGRAMA QUE TENHA FUNÇÃO VOTO, QUE RECEBA O ANO DE NASCIMENTO DA PESSOA E DIGA,
RETORNANDO UM VALOR LITERAL, INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO.

"""


def eleicoes(nascimento):
    """
    -> Verifica, pelo ano de nascimento, qual a situação eleitoral da pessoa.
    :param nascimento: ano de nascimento
    :return: valor literal = situação da pessoa
    """
    from datetime import datetime
    idade = datetime.now().year - nascimento
    if idade < 16:
        return f"Terá permissão de votar em {16-idade} anos. "
    elif idade < 18 or idade >= 65:
        return f"Seu voto é opcional."
    elif idade >= 18:
        return f"Seu voto será obrigatório por mais {65-idade} anos."


print("~"*30)
nasc = int(input("Qual seu ano de nascimento? "))
print(eleicoes(nasc))
