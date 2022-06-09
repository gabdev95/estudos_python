nome = str(input('Digite seu nome completo: '))
listaNome = nome.split()
firstName = listaNome[0]
lastName = listaNome.pop()
print('Nome completo: {}'.format(nome))
print('Primeiro nome: {}'.format(firstName))
print('Último nome: {}'.format(lastName))
