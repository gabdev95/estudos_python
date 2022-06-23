# Crie um programa onde o usuário possa digitar vários
# valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente

valores = lista_unica = list()
valores.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso...')
sim_nao = str(input('Deseja continuar? [S/N]'))
while True:
    if sim_nao in 'Ss':
        valores.append(int(input('Digite um valor: ')))
        print('Valor adicionado com sucesso...')
        sim_nao = str(input('Deseja continuar? [S/N]'))
        valores.sort()
        lista_unica = list(set(valores))
    else:
        break
print(valores)
