'''for c in range(1, 10):
    print(c)
print('fim')'''

'''c = 1
while c < 11:
    print(c)
    c += 1  # Equivale a c = c + 1
print('fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S, N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es)!'.format(par, impar))
