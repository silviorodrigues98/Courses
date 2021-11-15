aluno = {"NOME": str(input("Nome: "))}
aluno["MÉDIA"] = float(input(f"Média de {aluno['NOME']}: "))
if aluno["MÉDIA"] >= 7:
    aluno["SITUAÇÃO"] = "Aprovado"
elif 5 <= aluno["MÉDIA"] < 7:
    aluno["SITUAÇÃO"] = "Recuperação"
else:
    aluno["SITUAÇÃO"] = "Reprovado"
print("-="*30)
for k, v in aluno.items():
    print(f"  - {k} é igual a {v}")
