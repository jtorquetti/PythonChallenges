a = int(input('Quantos dias alugados? '))
q = float(input('Quantos Km Rodados? '))
d = (a * 60) + (q * 0.15)
print('O total a pagar e de R${:.2f}'.format(d))
