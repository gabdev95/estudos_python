# Faça um programa que leia um número inteiro e diga se ela é ou não um número primo

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[0;35m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Ele é PRIMO!')
else:
    print('Ele NÃO é PRIMO!')
