"""DESAFIO 011
ESCREVA UM PROGRAMA QUE LEIA A ALTURA E LARGURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E
A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2M²."""

lp = float(input('Digite a largura da parede'))
ap = float(input('Digite a altura da parede'))
area = lp * ap
qt = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(lp, ap, area))
print('E você vai precisar de {}litros de tinta para pinta-la'.format(qt))
