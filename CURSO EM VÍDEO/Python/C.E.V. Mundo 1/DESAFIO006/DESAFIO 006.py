print('Primeiro desafio, quer um programa que mostre um numero através de input \ne mostre seu sucessor e seu antecessor')
n1 = int(input('Digite aqui o número que por qualquer razão \nsem sentido vocÊ queira saber o antecessor e seu sucessor:'))
a1 = n1-1
s1 = n1+1
print('O sucessor de {:>2} é {:.5f}, e o antecessor é {:=^8}.'.format(n1, s1, a1))

('JÁ O SEGUNDO DESAFIO, QUER QUE EU DIGA QUAL O DOBRO,\nO TRIPLO E A RAIZ QUADRADA DE UM NÚMERO')
v1 = float(input('Diga um número, e eu MÁGICAMENTE direi algumas coisas sobre ele: '))
v2 = v1*2
v3 = v1*3
q1 = v1**(1/2)
print('OLHA QUE COISA! Descobri que:\nO dobro de {:>12} é {:.10f};\nO triplo de {:^11} é {:&^9};\nE sua raiz quadrada é:{}'.format(v1, v2, v1, v3, q1))

print('VAMOS AO TERCEIRO DESAFIO.\nESTE É MAIS SIMPLES.\nBASTA SOMAR DUAS NOTAS,\nE DAR A MÉDIA ENTRE ELAS.')
m1 = float(input('Primeiro semestre do aluno: '))
m2 = float(input('Segundo semestre do aluno '))
m3 = (m1+m2)/2
print('A média anual dos dois semestre é: {:<10}BUCETUDA'.format(m3))

print('HOJE TEM EXERCÍCIO PRA KRL, PORTANTO, AGORA VAMOS CONVERTER UNIDADES.')
u = float(input('Medida em metros ou em quilos: '))
cm = u*100
ml = u*1000
print('Espero que {:@^20} corresponda à {:>20} centntímetros.\nE que também corresponda à {:=^20} milimetros.'.format(u, cm, ml))
