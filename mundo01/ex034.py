""" ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONARIO E CALCULE O VALOR DO SEU
    AUMENTO.
    PARA SALARIOS SUPERIORES A R$ 1.250,00, CALCULE UM AUMENTO DE 10%. PARA OS INFERIORES OU
    IGUAIS, O AUMENTO É DE 15% """

sal = int(input('Qual o valor do salário atual do funcionário? R$ '))
if sal <= 1250:
    aum = sal + (sal / 100 * 15)
else:
    aum = sal + (sal / 100 * 15)
print('O novo salário passa a ser R$ {:.2f}'.format(aum))
