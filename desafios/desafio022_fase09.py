# Crie um progra que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúculas.
# Quantas letras ao td (sem considerar espaços).
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
print('Nome completo: {}.'.format(nome))
print('Nome completo em upper: {}'.format(nome.upper()))
print('Nome completo em lower: {}'.format(nome.lower()))
nomes = nome.replace(' ', '')
print('Seu nome tem {} letras (sem considerar os espaços).'.format(len(nomes)))
pnome = nome.split()
print('Seu primeiro nome é: {}.'.format(pnome[0]))
print('Seu primeiro nome possui {} letras.'.format(len(pnome[0])))
