# Faça um programa que leia uma frase e mostre
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).strip().upper()
contagem = frase.count('A')
print('A letra "A" aparece {} vezes.'.format(contagem))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))
