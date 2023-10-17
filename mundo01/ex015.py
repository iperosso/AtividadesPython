# ESCREVA UM PROGRAMA QUE LEIA A QUANTIDADE DE KM's PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS
# QUAIS ELE FOI ALUGADO E CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO
dias = int(input('Digite a quantidade de dias em que o carro foi alugado'))
km = float(input('Digite quantos KMs foram percorridos nesse período'))
aluguel = (dias * 60) + (km * 0.15)
print('O aluguel de {}dias e {}KMs rodados equivale a R${:.2f}'.format(dias, km, aluguel))
