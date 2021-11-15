v1 = int(input('Olá, estou aqui para auxilia-lo a somar números. Digite a primeira variável: '))
v2 = int(input('Ótimo! Agora digite o valor que vai ser somado à ela: '))
v3 = v1+v2
print('Veja! Somei os números para você')
print('A soma entre {} e {} resulta em {} '.format(v1, v2, v3))
print(type(v3))

t1 = input('Agora digite um algarismo qualquer para testar o comando IS ')
print(t1.isnumeric())
print(t1.isprintable())
print(t1.islower())
print(t1.isspace())
print(t1.istitle())