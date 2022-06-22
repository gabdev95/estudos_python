# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o progrma deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# [1] quantas pessoas tem mais de 18 anos.
# [2] quantos homens foram cadastrados.
# [3] quantas mulheres tem menos de 20 anos.

total_pessoas_maiores = total_homens = total_mulheres_20 = idade = 0
sexo = continuar = ''
while True:
    print('--' * 16)
    print('     CADASTRE UMA PESSOA     ')
    print('--' * 16)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] '))
    print('--' * 16)
    if idade > 18:
        total_pessoas_maiores += 1
    if sexo in 'Mm':
        total_homens += 1
    if sexo in 'Ff' and idade < 20:
        total_mulheres_20 += 1
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('====== FIM DO PROGRAMA ======')
print('Total de pessoas com mais de 18 anos cadastradas: {}'.format(total_pessoas_maiores))
print('Homens cadastrados: {}'.format(total_homens))
print('Mulheres com menos de 20 anos: {}'.format(total_mulheres_20))
