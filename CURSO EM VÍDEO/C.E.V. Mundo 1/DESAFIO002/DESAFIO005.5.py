print('JÁ PERDEU A GRAÇA AGORA É O ÚLTIMO MESMO')

s1 = float(input('Digite aqui seu salário atual: '))
s2 = float(input('Ótimo"Agora digite a porcentagem de seu aumento: '))
au = (s2+100)/100

print('Parabéns, funcionário! Seu novo salário será R${:.2f}'.format(au*s1))
