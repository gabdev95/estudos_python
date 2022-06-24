# Faça um programa que leia o nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# [1] Quantas pessoas foram cadastradas
# [2] Uma listagem com as pessoas mais pesadas.
# [3] Uma listagem com as pessoas mais leves.

temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {principal}')
print(f'Ao todo, foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}kg:', end=' ')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menor}kg:', end=' ')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
