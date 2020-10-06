l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
m = l * a
t = m / 2
print("Tenho uma parede de {} x {} no total de {} metros quadrados\nirei gastar {:.1f} litros de tinta para pintar toda a parede".format(l,a,m,t))
