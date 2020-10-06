print('='*32)
print('CONFEDERACAO NACIONAL DE NATACAO')
print('='*32)
a = int(input('Qual o ano do seu nascimento? '))
b = 2019 - a
if  b <= 9:
    print('Voce nasceu em {} e com a idade de {} anos voce se encaixa na categoria MIRIM'.format(a, b))
elif b <= 14 and b > 9:
    print('Voce nasceu em {} e com a idade de {} anos voce se encaixa na cetegoria INFANTIL'.format(a, b))
elif b <= 19 and b > 14:
    print('Voce nasceu em {} e com a idade de {} anos voce se encaixa na cetegoria JUNIOR'.format(a, b))
elif b <= 25 and b > 19:
    print('Voce nasceu em {} e com a idade de {} anos voce se encaixa na cetegoria SENIOR'.format(a, b))
else:
    print('Voce nasceu em {} e com a idade de {} anos voce se encaixa na cetegoria MASTER'.format(a, b))
