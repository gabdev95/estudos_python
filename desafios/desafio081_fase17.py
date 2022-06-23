# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# [1] Quantos números foram digitados.
# [2] A lista de valores, ordenada de forma decrescente.
# [3] Se o valor 5 foi digitado e está ou não na lista.

valores = []
valores.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso...')
sim_nao = str(input('Deseja continuar? [S/N] '))[0]
while True:
    if sim_nao in 'Ss':
        valores.append(int(input('Digite um valor: ')))
        print('Valor adicionado com sucesso...')
        sim_nao = str(input('Deseja continuar? [S/N] '))[0]
    else:
        break
valores.sort(reverse=True)
print('-=' * 30)
print(f'Foram digitados {len(valores)} números.')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 FOI DIGITADO e está na lista.')
else:
    print('O valor 5 NÃO FOI DIGITADO e não está na lista.')