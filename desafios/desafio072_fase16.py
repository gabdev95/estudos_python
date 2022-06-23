# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte. Seu programa deverá ler um número
# pelo teclado (entre 0 e 20) e mostrá-lo por extenso

contagem = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
            'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUIZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= numero <= 20:
        break
    else:
        numero = int(input('Opção inválida! Digite um número entre 0 e 20: '))
print(f'Você digitou o número {contagem[numero]}.')
