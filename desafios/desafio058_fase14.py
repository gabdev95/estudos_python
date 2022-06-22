# Melhore o jogo do DESAFIO 28 onde o computador 'pensa' em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

print('Oi! Aqui é o PC de novo!')
print('Tente adivinhar em que número, de 0 a 10, eu estou pensando!')
lista = list(range(10))
pc_escolhe = int(random.choice(lista))
print(pc_escolhe)
palpite = int(input('Digite aqui o seu palpite: '))
tentativas = 1
nao_adivinhou = True
if palpite == pc_escolhe:
    nao_adivinhou = False
    print('Você ACERTOU! Eu pensei no número {}.'.format(pc_escolhe))
    print('Você acertou em {} tentativa(s).'.format(tentativas))
while nao_adivinhou:
    print('Você ERROU! Tente novamente.')
    palpite = int(input('Digite aqui o seu palpite: '))
    tentativas += 1
    if palpite == pc_escolhe:
        nao_adivinhou = False
        print('Você ACERTOU! Eu pensei no número {}.'.format(pc_escolhe))
        print('Você acertou em {} tentativa(s).'.format(tentativas))
