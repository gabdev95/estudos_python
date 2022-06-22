# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# [1] qual é o total gasto na compra.
# [2] quantos produtos custam mais de R$1000.
# [3] qual é o nome do produto mais barato.

total = produtos_caros = posicao = mais_barato = 0
lista_produtos = []
lista_precos = []
print('--' * 16)
print('     LOJA BARATÃO     ')
print('--' * 16)
while True:
    nome_produto = str(input('Nome do produto: ')).strip()
    lista_produtos.append(nome_produto)
    preco_produto = int(input('Preço: R$ '))
    lista_precos.append(preco_produto)
    total = sum(lista_precos)
    mais_barato = min(lista_precos)
    posicao = lista_precos.index(mais_barato)
    continuar = str(input('Deseja continuar? [S/N] '))
    if preco_produto > 1000:
        produtos_caros += 1
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('--' * 16)
print('     FINAL DAS COMPRAS     ')
print('--' * 16)
print('O total da compra foi R${:.2f}'.format(total))
print('Compra de {} produto(s) acima de R$1000.00'.format(produtos_caros))
print('O produto mais barato foi {} que custa R${:.2f}'.format(lista_produtos[posicao], mais_barato))
