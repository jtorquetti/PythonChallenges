a = int(input('Qual a sua idade? '))
if a < 18:
    print('Falta {} ano/anos para voce se alistar, voce devera se alistar no ano de {}'.format(18 - a, (18 - a) + 2019))
elif a == 18:
    print('Voce tem a idade para se alistar no exercicito')
else:
    print('Voce esta {} ano/anos atrasado para o alistamento no exercito, voce deveria ter se aliastado no ano {}'.format(a - 18, 2019 - (a - 18)))