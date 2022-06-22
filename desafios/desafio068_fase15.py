# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
jogador = computador = soma = contador = 0
total = ''
while True:
    computador = randint(0, 20)
    jogador = int(input('Digite um valor: '))
    par_ou_impar = str(input('Par ou Ímpar? [P/I] '))
    soma = jogador + computador
    if soma % 2 == 0:
        total = 'DEU PAR'
    else:
        total = 'DEU ÍMPAR'
    print('--' * 15)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma} {total}')
    print('--' * 15)
    if par_ou_impar in 'Pp' and soma % 2 == 0 or par_ou_impar in 'Ii' and soma % 2 != 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('--' * 15)
        contador += 1
    else:
        print('Você PERDEU!')
        print('-=' * 15)
        break
print('GAME OVER! Você venceu {} vez(es) durante o jogo!'.format(contador))
