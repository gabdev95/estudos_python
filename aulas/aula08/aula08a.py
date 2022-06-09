from math import sqrt, floor
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, floor(raiz)))
print(emoji.emojize('Olá, mundo! :earth_americas:', language='alias'))
