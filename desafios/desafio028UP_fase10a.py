# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random


lista = list(range(100))
print('Oi, eu sou o PC! Você gostaria de jogar? Estou pensando em um número entre 0 e 5.')
naoAdivinhou = True
escolhido = str(random.choice(lista))
print('Você consegue adivinhar que número é esse?')
while naoAdivinhou:
    escolhaUsuario = str(input('Digite seu palpite: '))
    if escolhaUsuario == escolhido:
        print('Você VENCEU! Eu pensei mesmo no número {}.'.format(escolhido))
        naoAdivinhou = False
    else:
        if escolhaUsuario > escolhido:
            print('Você escolheu um número maior. Tente novamente.')
        else:
            print('Você escolheu um número menor. Tente novamente.')
