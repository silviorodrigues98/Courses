print('Conversor de unidades que bugou para um krl')
print()
print()
n1 = float(input('Coloque seu número, e o converterei em diversas unidades: '))
km = (n1 / 1000)
hm = n1 / 100
dcm = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
print('{}km\n{}hm\n{}dcm\n{}dm\n{}cm\n{}mm'.format(km, hm, dcm, dm, cm, mm))
