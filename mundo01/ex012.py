""" FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O SEU VALOR COM UM DESCONTO DE 15%"""

vi = float(input('Digite o preço do produto'))
desc = vi - (vi / 100 * 15)
print('O valor com desconto fica R${}'.format(desc))
