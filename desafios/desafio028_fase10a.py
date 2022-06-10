# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

lista = [0, 1, 2, 3, 4, 5]
escolhido = str(random.choice(lista))
print('Oi, eu sou o PC! Você gostaria de jogar? Estou pensando em um número entre 0 e 5.')
print('Você consegue adivinhar que número é esse?')
escolhaUsuario = str(input('Digite seu palpite: '))
if escolhaUsuario == escolhido:
    print('Você VENCEU! Eu pensei mesmo no número {}.'.format(escolhido))
else:
    print('Você PERDEU. Eu pensei no número {} :('.format(escolhido))
print('Até a próxima!')
