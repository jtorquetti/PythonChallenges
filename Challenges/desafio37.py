a = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversao:
[1]converter para BINARIO
[2]converter para OCTAL
[3]converter para HEXADECIMAL''')
b = int(input('Qual a base de conversao? '))
if b == 1:
    print('{} convertido para BINARIO e igual a {}'.format(a, bin(a)[2:]))
elif b == 2:
    print('{} convertido para OCTAL e igual a {}'.format(a, oct(a)[2:]))
elif b == 3:
    print('{} convrtido para HEXADECIMAL e igual a {}'.format(a, hex(a)[2:]))
else:
    print('Opcao invalida!')
