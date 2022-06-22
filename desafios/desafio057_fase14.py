# Faça um programa que leia o sexo de uma pessoa, mas só aceite valores "M" ou "F".
# Caso esteja, peça a digitação novamente até ter um valor correto

sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()
while sexo not in 'FfMm':
    print('Opção Inválida!')
    sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()
print('Opção validada! Sexo {}.'.format(sexo))
