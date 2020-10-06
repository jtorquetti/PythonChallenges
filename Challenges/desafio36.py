print('='*51)
print('Bem vindo ao simulador de financiamento de imovel!')
print('='*51)
a = float(input('Qual o valor da Casa que voce quer comprar? '))
b = float(input('Qual e o seu salario mensal? '))
c = int(input('Em quantos anos voce quer financiar a casa? '))
d = a / (c * 12)
e = b * 30 / 100
if d <= e:
    print('Seu emprestimo no valor de {:.2f}R$ para pagar em {:.0f} meses de {:.2f}R$ por mes foi aprovado, PARABENS!'.format(a,c*12,d))
elif d >= e:
    print('O valor da parcela nao pode exceder 30% da sua renda mensal, por essa razao o emprestido foi negado, DESCULPE!')
