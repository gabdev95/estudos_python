# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando estrutura while

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')
