# Crie um progra que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúculas.
# Quantas letras ao td (sem considerar espaços).
# Quantas letras tem o primeiro nome

nome = str(input('Digite sem nome completo: ')).strip()  # função strip() elimina os espaços antes e depois
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é "{}".'.format(nome.upper()))
print('Seu nome em letras minúsculas é "{}".'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
# ou
separa = nome.split()
print('Seu primeiro nome é "{}" e ele possui {} letras.'.format((separa[0]), len(separa[0])))
