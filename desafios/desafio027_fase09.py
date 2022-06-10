# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
listaNome = nome.split()
firstName = listaNome[0]
lastName = listaNome.pop()
print('Nome completo: {}'.format(nome))
print('Primeiro nome: {}'.format(firstName))
print('Último nome: {}'.format(lastName))
