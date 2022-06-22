# Escreva um programa que leia um n[umero n inteiro qualquer e
# mostre na tela os n primeiros elementos de uma sequencia fibonacci

termos = int(input('Quantos termos você que mostrar? '))
print('~' * 40)
termo1 = 0
termo2 = 1
print('{} -> {}'.format(termo1, termo2), end=' ')
cont = 3
while cont <= termos:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end=' ')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('-> FIM')

