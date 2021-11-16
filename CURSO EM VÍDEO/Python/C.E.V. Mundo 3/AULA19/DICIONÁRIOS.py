#  pessoas = dict()
#  pessoas = {}
pessoas = {"nome": "Gustavo", "sexo": "M", "Idade": 22}
print(pessoas)
print(pessoas["nome"])
print(pessoas["Idade"])
print(f"O {pessoas['nome']} tem {pessoas['Idade']} anos.")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
del pessoas["sexo"]  # apaga o elemento
for k, v in pessoas.items():
    print(f"{k} = {v}")
pessoas["nome"] = "Leandro"  # Substitui o nome por outro.
print(pessoas["nome"])