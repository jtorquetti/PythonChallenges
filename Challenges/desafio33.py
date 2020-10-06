a = float(input('Primeiro numero: '))
b = float(input('Segundo numero: '))
c = float(input('Terceiro numero:'))
if a <= b and a <= c:
    ma = a
if b <= a and b <= c:
    ma = b
if c <= a and c <= b:
    ma = c
if a >= b and a >= c:
    me = a
if b >= a and b >= c:
    me = b
if c >= a and c >= a:
    me = c
print('O menor numero e {:.0f} e o maior e {:.0f}'.format(ma, me))