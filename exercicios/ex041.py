# A confederação de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: sênior
# Acima: master

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 20:
    print('Classificação: SÊNIOR')
elif idade > 20:
    print('Classificação: MASTER')

