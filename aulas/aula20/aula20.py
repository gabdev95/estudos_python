# def mostra_linha():
#     print('=' * 50)


# mostra_linha()
# print('CURSO EM VÍDEO'.center(50))
# mostra_linha()
# mostra_linha()
# print('Aprenda Python!'.center(50))
# mostra_linha()
# mostra_linha()
# print('Gabriele'.center(50))
# mostra_linha()

# def mensagem(msg):
#     print('=' * 50)
#     print(msg)
#     print('=' * 50)


# mensagem('Sistema de Alunos'.center(50))
# mensagem('Gabriele Medeiros'.center(50))

# def soma(a, b):
#     s = a + b
#     print(s)


# programa principal
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)
# soma(4, 1)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
