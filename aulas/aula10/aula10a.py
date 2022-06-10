# nome = str(input('Qual é o seu nome? ')).strip()
# lnome = nome.lower()
# if lnome == 'gabriele':
#     print('Que nome lindo!')
# else:
#     print('Seu nome é tão normal.')
# print('Boa semana, {}.'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m >= 7.0:
    print('Você está aprovado.')
else:
    print('Você está reprovado.')
