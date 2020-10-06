a = (float(input('Primeira nota: ')))
b = (float(input('Segunda nota:')))
c = (a + b) / 2
if c < 5.0:
    print('Sua media e {}, Reprovado'.format(c))
elif c >= 5.0 and c < 6.9:
    print('Sua media e {}, RECUPERACAO'.format(c))
else:
    print('Sua media e {}, Aprovado'.format(c))