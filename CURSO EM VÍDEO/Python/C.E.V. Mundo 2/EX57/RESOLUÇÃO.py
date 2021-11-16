sexo = str(input("Qual seu sexo?[M/F] ")).strip().upper()[0] # ISSO FAZ ELE PEGAR SÓ O M OU F
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:[M/F]')).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))
idade = int(input("Informe sua idade: "))
print(sexo)
