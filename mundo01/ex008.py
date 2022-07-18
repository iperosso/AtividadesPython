"""DESAFIO 008
ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS."""

vi = float(input('Digite o valor em metros para ser convertido'))
m = vi
dm = vi * 10
cm = dm * 10
mm = cm * 10
dam = m / 10
hm = dam / 10
km = hm / 10
print('A quantidade de {}metros equivale a {}mm, {}cm, {}dm, {}dam, hm{}, {}km'.format(m, mm, cm, dm, dam, hm, km))
