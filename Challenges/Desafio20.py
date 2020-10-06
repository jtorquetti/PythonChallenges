import random
a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ')
lista = [a,b,c,d]
n = random.shuffle(lista)
print('Os alunos deveram entregar os trabalhos na ordem {}'.format(n))
print(lista)