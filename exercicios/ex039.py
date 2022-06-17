# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:
# Se ele ainda vai tirar o título de eleitor.
# Se ele já tem idade mínima para tirar o título de eleitor
# Se já é obrigatório ele tirar o título de eleitor
# Se já passou do tempo de tirar o título de eleitor
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que tirar o titulo de eleitor IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para tirar o título de eleitor.'.format(saldo))
    ano = atual + saldo
    print('Seu título de eleitor será obrigatório em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você tirou seu título de eleitor há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu título de eleitor foi obrigatório a partir de {}.'.format(ano))
