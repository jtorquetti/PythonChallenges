from random import randint
from time import sleep
computador = randint(0,5) #faz o computador 'PENSAR'
print( '-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('PARABENS! Voce Venceu')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}'.format(computador,jogador))