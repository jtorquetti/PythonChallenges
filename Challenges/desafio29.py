a = float(input('Qual e a velocidade atual do carro? '))
if a >= 80:
    print('Voce estava a {:.0f}Km/h e excdeu o limite de 80Km/h e foi multado em {:.2f}R$'.format(a, (a-80)*7))
else:
    print('Tenha um boma dia dirija com seguranca!')