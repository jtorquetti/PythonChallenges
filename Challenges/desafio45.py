import random
itens = ('Pedra', 'Papel', 'Tesoura')
print('='*13)
print('JOKENPO GAME!')
print('='*13)
print('Escolha uma das opcoes!')
print('''[0]Pedra
[1]Papel
[2]Tesoura''')
user = int(input('Voce escolhe? '))
print('''JO
KEN
PO!''')
computador = random.randint(0, 2)
print('O Computador jogou {}'.format(itens[computador]))
print('Voce jogou {}'.format(itens[user]))
if computador == 0:
    if user == 0:
        print('Empate')
    elif user == 1:
        print('User venceu!')
    elif user == 2:
        print('Computador venceu!')
    else:
        print('Jogada Invalida')
elif computador == 1:
    if user == 0:
        print('Computador venceu!')
    elif user == 1:
        print('Empate!')
    elif user == 2:
        print('User venceu!')
    else:
        print('Jogada Invalida')
elif computador == 2:
    if user == 0:
        print('User venceu!')
    elif user == 1:
        print('Computador venceu!')
    elif user == 2:
        print('Empate!')
    else:
        print('Jogada Invalida')




