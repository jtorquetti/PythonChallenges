p = float(input('Preco do produto = R$'))
v = p * 0.90
f = p * 1.05
x = f / 12
print('Preco do produto = R${:.2f}'.format(p))
print('Preco do produto a vista = R${:.2f}'.format(v))
print('Preco do produto parcelado em 12x = R${:.2f} por mes, total = R${:.2f}'.format (x,f))