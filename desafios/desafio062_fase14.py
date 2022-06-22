# Melhore o desafio 061, perguntando para o usuário se ele quer
# mostrar mais alguns termo. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
termo = primeiro_termo
total = 0
mais = 10
cont = 1
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você gostaria de ver a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
