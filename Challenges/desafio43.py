p = float(input('Qual o seu peso? '))
a = float(input('Qual a sua altura? '))
imc = float(p / (a ** 2))
print('O IMC dessa pessoa e de {:.2f}'.format(imc), end=' ')
if imc < 18.5:
    print('Voce esta abaixo do peso')
elif imc >= 18.5 and imc <= 24:
    print('Seu peso e o ideal')
elif imc >= 25 and imc <= 29:
    print('Voce esta sobrepeso')
elif imc >= 30 and imc <= 39:
    print('Voce esta Obeso')
else:
    print('Voce esta Obeso morbido')
