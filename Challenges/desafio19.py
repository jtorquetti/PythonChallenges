from random import choice
a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input("Quarto Aluno: ")
alunos = [a,b,c,d]
esc = choice(alunos)
print('O aluno escolhido foi : {}'.format(esc))