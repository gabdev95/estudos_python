nome = str(input('Digite seu nome completo: '))
procuraSilva = 'Silva' in nome

if procuraSilva is True:
    print('Você possui "Silva" no nome.')

else:
    print('Você não possui "Silva" no nome.')
