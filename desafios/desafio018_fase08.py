import math
ang = float(input('Digite um angulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O seno de {} é igual a {:.2f}'.format(ang, sen))
print('O cosseno de {} é igual a {:.2f}'.format(ang, cos))
print('A tangente de {} é igual a {:.2f}'.format(ang, tg))
