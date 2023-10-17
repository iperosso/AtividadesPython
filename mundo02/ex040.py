# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A SUA MEDIA, MOSTRANDO UMA
# MENSAGEM NO FINAL, DE ACORDO COM A MEDIA ATINGIDA:
# >MEDIA ABAIXO DE 5.0: REPROVADO
# >MEDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# >MEDIA 7.0 OU SUPERIOR: APROVADO
n1 = float(input('Nota do primeiro semestre'))
n2 = float(input('Nota do segundo semestre'))
media = (n1 + n2) / 2
if media < 5.0:
    print('Reprovado, sua media foi muito baixa')
elif media < 6.9:
    print('Recuperação')
else:
    print('Aprovado')
