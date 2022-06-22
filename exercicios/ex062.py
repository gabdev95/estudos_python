# Melhore o desafio 061, perguntando para o usuário se ele quer
# mostrar mais alguns termo. O programa encerra quando ele disser que quer mostrar 0 termos.

print('Gerador de P.A.: ')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))
termo = primeiro
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
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
