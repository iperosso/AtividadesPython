""" ESCREVA UM PROGRAMA PARA APROVAR O EMPRESTIMO BANCARIO PARA COMPRAR UMA CASA. PERGUNTE
    O VALOR DA CASA, O SALARIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
    A PRESTAÇÃO MENSAL NÃO PODE EXCEDER 30% DO SALARIO OU ENTÃO O EMPRESTIMO SERÁ NEGADO."""

emp = int(input('Qual o valor do imóvel a ser financiado? '))
sal = int(input('Qual o salário bruto do comprador? '))
tam = int(input('Em quantos anos será feito o financiamento? '))
lim = (sal / 100) * 30
mens = emp / (tam * 12)
if mens > lim:
    print('Financiamento Negado')
else:
    print('Financiamento Aprovado')
