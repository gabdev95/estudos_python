# Crie um programa que leia um número inteiro e mostre na tela
# se ele é par ou ímpar

numero = float(input('Digite um número e descubra se ele é ímpar ou par: '))
resto = numero % 2
if resto == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))
print('Operação finalizada!')
