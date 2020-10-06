from math import radians, sin, cos, tan
ang = float(input('coloque aqui seu angulo: '))
co = cos(radians(ang))
si = sin(radians(ang))
ta = tan(radians(ang))
print("Seu angulo e {}, seu cosseno {:.2f}, seu seno {:.2f} e sua tangente {:.2f}".format(ang,co,si,ta))