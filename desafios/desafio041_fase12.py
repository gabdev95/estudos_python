# A confederação de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: sênior
# Acima: master

from datetime import date
ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade <= 9:
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Categoria: MIRIM')
elif 9 < idade <= 14:
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Categoria: INFANTIL')
elif 14 < idade <= 19:
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Categoria: JÚNIOR')
elif 19 < idade <= 20:
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Categoria: SÊNIOR')
else:
    print('O atleta tem {} anos de idade.'.format(idade))
    print('Categoria: MASTER')
