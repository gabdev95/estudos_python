# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores

from datetime import date
ano_atual = date.today().year
total_maioridade = 0
total_menoridade = 0
for datas in range(1, 8):
    data_nasc = int(input('Qual é o ano de nascimento da {}ª pessoa? '.format(datas)))
    idade = ano_atual - data_nasc
    if idade >= 21:
        print('Essa pessoa tem {} anos e atingiu a MAIORIDADE.'.format(idade))
        total_maioridade += 1
    else:
        print('Essa pessoa tem {} anos e NÃO atingiu a MAIORIDADE.'.format(idade))
        total_menoridade += 1
print('=-' * 30)
print('''Nesse grupo existem {} pessoas que atingiram a maioridade
e {} pessoas que não atingiram a maioridade.'''.format(total_maioridade, total_menoridade))
print('=-' * 30)
