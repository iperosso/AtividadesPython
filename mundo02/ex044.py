# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO
# O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# >A VISTA NO DINHEIRO 10% DE DESCONTO
# >DEBITO A VISTA 5% DE DESCONTO
# >EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# >3X OU MAIS: 20% DE JUROS
vp = float(input('Valor do produto'))
print('''Forma de pagamento
[ 1 ] Dinheiro
[ 2 ] Debito
[ 3 ] Até 3x no Crédito
[ 4 ] Até 10x no Crédito''')
fp = int(input('Selecione a opção'))
if fp == 1:
    desc = vp - (vp / 100 * 15)
    print('[ Dinheiro selecionado ] você teve um desconto de 15%, o valor do produto ficou {}'.format(desc))
elif fp == 2:
    desc = vp - (vp / 100 * 5)
    print('[ Débito selecionado ] vocÇe teve um desconto de 5%, o valor do produto ficou {}'.format(desc))
elif fp == 3:
    print('''Selecione a quantidade de parcelas:
    [ 2 ] Parcelas
    [ 3 ] Parcelas''')
    qtp = int(input('Selecione a opção:'))
    if qtp == 2 or 3:
        vpc = vp / qtp
        print('O pagamento será {}x de {:.2f}'.format(qtp, vpc))
    else:
        print('Opção inválida, tente novamente.')
elif fp == 4:
    print('''Selecione a quantidade de parcelas:
    [ 4 ] Parcelas
    [ 5 ] Parcelas
    [ 6 ] Parcelas
    [ 7 ] Parcelas
    [ 8 ] Parcelas
    [ 9 ] Parcelas
    [ 10 ] Parcelas''')
    qtp = int(input('Selecione a opção'))
    if 4 <= qtp <= 10:
        vpc = (vp + ((vp / 100) * (qtp * 2))) / qtp
        print('A compra será feita em {} parcelas de R$ {} cada'.format(vp, vpc))
    else:
        print('Opção errada, inicie novamente')
