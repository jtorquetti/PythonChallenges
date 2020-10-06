from math import hypot
a = float(input("Comprimento do cateto oposto: "))
b = float(input("Comprimento do cateto adjacente: "))
h = hypot(a,b)
print("O valor da hipotenusa e {:.2f}cm".format(h))

