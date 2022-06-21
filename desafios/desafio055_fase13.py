# Faça um programa que leia o peso de cinco pessoas.
# No final mostre qual foi o maior e o menor peso lidos.

lista_pesos = []
maior_peso = 0
menor_peso = 0
for peso in range(1, 6):
    pesos = float(input('Digite o peso da {}ª pessoa: '.format(peso)))
    lista_pesos.append(pesos)
    maior_peso = max(lista_pesos, key=float)
    menor_peso = min(lista_pesos, key=float)
print('-=' * 20)
print('O maior peso do grupo é {:.1f}kg.'.format(maior_peso))
print('O menor peso do grupo é {:.1f}kg.'.format(menor_peso))
print('-=' * 20)
