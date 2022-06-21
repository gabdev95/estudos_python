# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores

from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade >= 21:
        print('Essa pessoa atingiu a MAIORIDADE.')
        total_maior += 1
    else:
        print('Essa pessoa NÃO antigiu a MAIORIDADE.')
        total_menor += 1
print('Existem {} pessoas que que atingiram a MAIORIDADE.'.format(total_maior))
print('Existem {} pessoas que NÃO  atingiram a MAIORIDADE.'.format(total_menor))
