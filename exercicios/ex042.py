# refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
# Equilátero: todos os lados semelhantes
# Isósceles: dois lados semelhantes
# Escaleno: todos os lados diferentes

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
print('-=' * 20)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end= '')
    if reta1 == reta2 == reta3:
        print(' EQUILÁTERO.')
    elif reta1 != reta2 != reta3 != reta1:
        print(' ESCALENO.')
    else:
        print(' ISÓSCELES.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
print('-=' * 20)

