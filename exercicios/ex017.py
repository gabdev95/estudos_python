import math
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(catop, catad)
print('\n**************************************\n')
print('Considerando os comprimentos: \nCateto oposto: {}\nCateto adjacente: {}'.format(catop, catad))
print('\n**************************************\n')
print('O comprimento da hipotenusa é {:.2f}'.format(hip))
print('\n**************************************\n')
