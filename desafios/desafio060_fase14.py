# Faça um programa que leia um número qualquer e mostre o seu fatorial

num = int(input('Fatorial de: '))
resultado = 1
cont = 1
while cont <= num:
    resultado *= cont
    cont += 1
print('{}! = {}'.format(num, resultado))
