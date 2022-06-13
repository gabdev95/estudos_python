# Desenvolva um programa que leia o comprimento de 3 retas e diga ao
# usuário se elas podem ou não formar um triângulo

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
maior = reta1
somaOutras = reta2 + reta3
if reta2 > maior:
    maior = reta2
    somaOutras = reta1 + reta3
if reta3 > maior:
    maior = reta3
    somaOutras = reta1 + reta2

if somaOutras > maior:
    print('O comprimento das retas permite formar um triângulo.')
else:
    print('O comprimento das retas não permite formar um triângulo.')
