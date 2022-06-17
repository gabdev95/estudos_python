# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:
# Se ele ainda vai tirar o título de eleitor.
# Se ele já tem idade mínima para tirar o título de eleitor
# Se já é obrigatório ele tirar o título de eleitor
# Se já passou do tempo de tirar o título de eleitor
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade < 16:
    print('Você ainda não tem idade para tirar o título de eleitor.')
    falta = 16 - idade
    print('Faltam {} ano(s) para atingir a idade mínima.'.format(falta))
elif 16 <= idade < 18:
    print('Você ainda não atingiu a maior idade!')
    print('Mas, como você tem {} anos, já é possível tirar o título de eleitor.'.format(idade))
elif idade == 18:
    print('Você tem {} anos. É OBRIGATÓRIO tira o título de eleitor!'.format(idade))
elif 18 < idade < 70:
    passou = idade - 18
    print('Faz/fazem {} ano(s) que você já é de maior.'.format(passou), end='')
    print(' Tirar o título de eleitor é OBRIGATÓRIO para você.')
else:
    print('Você não é mais obrigado a votar.')
print(idade)
