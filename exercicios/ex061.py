# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando estrutura while

print('Gerador de P.A.: ')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')
