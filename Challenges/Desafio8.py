m = float(input('Quantos Metros?'))
cm = m * 100
mm = m * 1000
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('Kilometros = {:.0f}km\nHectometro = {:.0f}hm\nDecametro = {:.0f}dam\nMetro = {:.0f}m\nDecimetro = {:.0f}dm\nCentimetro = {:.0f}cm\nMilimetro = {:.0f}mm'.format(km,hm,dam,m,dm,cm,mm))
