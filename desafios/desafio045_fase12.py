# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

print('Oi! Aqui é o PC de novo!')
print('Vamos jogar jokenpô?')
nao_valida = True
while nao_valida:
    jogar = str(input('Digite "s" para sim e "n" para não: ')).strip().lower()
    if jogar == 's':
        nao_valida = False
        pc = randint(0, 2)
        print('-=' * 20)
        print('Oba, vamos jogar!!')
        sleep(2)
        print('-=' * 20)
        print('Digite 0 para pedra')
        print('Digite 1 para papel')
        print('Digite 2 para tesoura')
        print('-=' * 20)
        sleep(2)
        escolhido_jogador = 'NADA'
        escolhido_pc = 'NADA'
        jogador = int(input('Pedra, papel ou tesoura? '))
        print('-=' * 20)
        if jogador == 0:
            escolhido_jogador = 'PEDRA'
        elif jogador == 1:
            escolhido_jogador = 'PAPEL'
        elif jogador == 2:
            escolhido_jogador = 'TESOURA'
        else:
            print('Não é uma opção válida')

        if pc == 0:
            escolhido_pc = 'PEDRA'
        elif pc == 1:
            escolhido_pc = 'PAPEL'
        elif pc == 2:
            escolhido_pc = 'TESOURA'

        if jogador == pc:
            print('Eu escolhi {} e você escolheu {}. EMPATAMOS'.format(escolhido_pc, escolhido_jogador))
        elif jogador == 0 and pc == 1 \
                or jogador == 1 and pc == 2 \
                or jogador == 2 and pc == 0:
            print('Eu escolhi {} e você escolheu {}. VOCÊ PERDEU'.format(escolhido_pc, escolhido_jogador))
        elif pc == 0 and jogador == 1 \
                or pc == 1 and jogador == 2 \
                or pc == 2 and jogador == 0:
            print('Eu escolhi {} e você escolheu {}. VOCÊ GANHOU'.format(escolhido_pc, escolhido_jogador))
        print('-=' * 20)
    elif jogar == 'n':
        nao_valida = False
        print('-=' * 20)
        print('Aah. Que pena :(')
        print('-=' * 20)
    else:
        print('-=' * 20)
        print('Digite uma opção válida.')
        print('-=' * 20)
        nao_valida = True
