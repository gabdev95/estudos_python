# Crie um programa que leia o nome de uma pessoa e diga
# se ela tem "Silva" no nome

nome = str(input('Digite seu nome completo: ')).strip()
procuraSilva = 'Silva' in nome

if procuraSilva is True:
    print('Você possui "Silva" no nome.')

else:
    print('Você não possui "Silva" no nome.')
