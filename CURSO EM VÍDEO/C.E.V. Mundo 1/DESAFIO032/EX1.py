# ANO BISSEXTO VACILEI
print('Bem vindo à outro medidor muito útil!!! ')
print()

ano = int(input('Diga o ano que está curioso: '))
print()

bis = ano % 4

if bis == 0:
    print('NOSSA! Que coincidência, justo este ano é um ano bissexto')
else:
    print('Como já imaginava...você nao sabe achar anos bissextos ')
print()
print('Até logo!')