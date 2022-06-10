# Faça um desafio que leia um ano mostre se é bissexto.

ano = int(input('Digite um ano e descubra se ele é um ano bissexto: '))
div = ano % 4
if div == 0:
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))