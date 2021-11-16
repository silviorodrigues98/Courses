sal = float(input("Qual é o salário do funcionário?R$ "))

if sal <= 1250:
    rea = sal + (sal*15/100)
else:
    rea = sal + (sal*10/100)
print('O novo salário será de:R$ {:.2f} '.format(rea))
