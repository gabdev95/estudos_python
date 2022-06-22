# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

from time import sleep

valor = 0
while True:
    print('~' * 40)
    sleep(1)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('~' * 40)
    if valor < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{valor} x {c:2} = {valor * c:2}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre')
