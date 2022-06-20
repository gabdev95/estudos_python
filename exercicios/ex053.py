# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()  # retirou os espaços e deixou tudo em maiúsculo
palavras = frase.split()  # Separou em vetores/palavras
junto = ''.join(palavras)  # Uniu as palavras
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]  # fez o inverso da string
if junto == inverso:
    print('A frase "{}" é PALÍNDROMO'.format(frase))
else:
    print('A frase "{}" NÃO é PALÍNDROMO'.format(frase))
