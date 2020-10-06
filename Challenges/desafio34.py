a = float(input('Qual o seu salario? '))
if a >= 1251:
    print("\033[31mSeu salario e\033[m \033[1;30;41m{:.2f}R$\033[m \033[31me voce recebera um almento de 10% e seu salario sera\033[m \033[1;30;41m{:.2f}R$\033[m".format(a, (a*0.10)+a))
else:
    print("\033[31mSeu salario e\033[m \033[1;30;41m{:.2f}R$\033[m \033[31me voce recebera um almento de 15% e seu salario sera\033[m \033[1;30;41m{:.2f}R$\033[m".format(a, (a*0.15)+a))