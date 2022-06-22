# Faça um programa que leia o sexo de uma pessoa, mas só aceite valores "M" ou "F".
# Caso esteja, peça a digitação novamente até ter um valor correto

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
#idade = int(input('Informe sua idade: '))
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido! Informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
