# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num  # equivale a soma = soma + 1
        cont = cont +1  # equivale a cont += 1
print('Você informou {} número(s) par(es) e a soma dele(s) foi {}'.format(cont, soma))
