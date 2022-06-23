# Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi o
# maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-' * 50)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} e sua posição foi a {valores.index(max(valores))}.')
print(f'O menor valor digitado foi {min(valores)} e sua posição foi a {valores.index(min(valores))}.')
print('-' * 50)
