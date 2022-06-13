# TESTES
# teste 1 letra branca fundo vermelho
# \033[0;30;41m
# teste 2 letra amarela fundo azul
# \033[4;33;44m
# teste 3 letra roxa fundo amarelo
# \033[1;35;43m
# teste 4 letra branca fundo verde
# \033[30;42m
# teste 5 letra branca fundo preto (padrão)
# \033[m
# teste 6 letra preta fundo branco
# \033[7;30m

print('\033[1;33;44mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[1;35m{}\033[m e \033[1;31m{}\033[m.'.format(a, b))

nome = 'Gabriele'
print('Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
