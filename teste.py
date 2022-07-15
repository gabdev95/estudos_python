'''s = 0
x = 0
while x < 3:
    x = x + 1
    s = s + x
print(s)

str = 'abcdef'
print(str[1:len(str)-3])

a = 'python é muito fácil'
print(a[:-5])

str2 = 'gfedcba'
print('Valor da substring = %s' %(str2[2:5].upper()))

w = 'bcdefg'
print(w[::2])

i = 'abcdefgh'
print(str.find('a',2))

a = ((2 + 3) - (5 * 8) / 4)
b = ((7 ** 2) * (4 / 2))
c = 26 % 7
soma = a + b + c
print(soma)

q = 'prova'
print(3 * q)

p = list(range(11))
d = [x for x in p if (x-1) ** 2 > 3]
print([x for x in d if x % 2 != 0])

g = 2 ** 16
print(g)'''

'''# sequencias e somatórios
ax = int(input('Digite o valor de n: '))
formula = 2 * (-3) ** ax + (5 ** ax)
teste1 = (-3) ** ax
teste2 = 5 ** ax
print(formula)
print(teste1)
print(teste2)'''

'''ai = int(input('Digite o valor de n: '))
formula2 = 2 ** ai - 1
print(formula2)'''
from math import floor
ax = int(input('Digite o valor de n: '))
formula = 1 - (-1) ** ax
print(floor(formula))
