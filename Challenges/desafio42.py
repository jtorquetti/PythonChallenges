print('\33[1;45;40m-=\33[m'*20)
print('\33[4;36;41mAnalisador de Triangulos\33[m')
print('\33[1;45;40m-=\33[m'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR Triangulo', end=' ')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR Triangulo')