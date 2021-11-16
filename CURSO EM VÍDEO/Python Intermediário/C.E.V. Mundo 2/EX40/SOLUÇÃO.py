
n1 = float(input('Primeir nota: '))
n2 = float(input('Segunda nota: '))
m1  = (n1+n2)/2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, m1))
if m1 >= 5 and m1 <7:
    print('O aluno está em recuperação')
elif m1 < 5:
    print('O aluno está reprovado')
else:
    print('O aluno está APROVADO')
