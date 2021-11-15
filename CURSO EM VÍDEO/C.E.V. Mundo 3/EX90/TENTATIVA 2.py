""" PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO SUA SITUAÇÃO. APROVADO OU REPROVADO.
GUARDAR TUDO ISSO EM UM DICIONÁRIO E MOSTRAR RESULTADO."""


aluno = {"nome": str(input("Nome: ")).title().strip()}
aluno["media"] = float(input(f"Média do(a) {aluno['nome']}: "))
for tipo, valor in aluno.items():
    print(f"{tipo} é igual a {valor}")
if aluno["media"] >= 7:
    print("Situação é igual a Aprovado. ")
else:
    print("Situação é igual a Reprovado. ")
