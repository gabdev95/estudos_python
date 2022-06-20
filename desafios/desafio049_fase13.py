# Refaça o desafio 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for

n1 = int(input('Digite um número inteiro: '))
print('A tabuada de {} é: '.format(n1))
for c in range(1, 11):
    print('{} * {} = '.format(n1, c), (c * n1), ';')
