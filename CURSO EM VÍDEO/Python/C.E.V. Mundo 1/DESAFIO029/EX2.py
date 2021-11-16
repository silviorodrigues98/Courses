vel = float(input('Qual é a velocidade do carro?Km/h '))
if vel > 80:

    mul = (vel - 80) * 7
    print('ATENÇÃO!!! Você ultrapassou o limite de segurança, e será multado no valor de R${:.2f}'.format(mul))

print('Tenha um bom dia! Diria com segurança!')



