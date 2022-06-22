# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição parada.
# No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag)

num = 0
contador = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, soma))