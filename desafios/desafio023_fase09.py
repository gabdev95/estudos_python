# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados

num = str(input('Digite um número entre 0 e 9999: '))
print('Unidade: ' + num[3])
print('Dezena: ' + num[2])
print('Centena: ' + num[1])
print('Milhar: ' + num[0])

# Esse códdigo não lê número sem milhar... Código correto no ex023!!
