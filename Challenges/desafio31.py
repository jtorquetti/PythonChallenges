a = float(input('Qual a distancia da sua viagem? '))
if a <= 200:
    print('Sua passagem custara {:.2f}R$'.format(a*0.50))
else:
    print('Sua Passagem custara {:.2f}R$'.format(a*0.45))