# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Qual é o preço do produto? R$'))
print('-=' * 20)
print('Para a forma de pagamento: ')
print('Digite 1 para pagamento a vista em dinheiro ou cheque.')
print('Digite 2 para pagamento a vista no cartão.')
print('Digite 3 para pagamento em 2x no cartão.')
print('Digite 4 para pagamento em 3x ou mais no cartão.')
print('-=' * 20)
forma_pagamento = int(input('Qual será a forma de pagamento? '))
if forma_pagamento == 1:
    pagamento = 'pagamento à vista em dinheiro ou cheque'
    valor = preco - (preco * 10 / 100)
    print('O valor do produto será R${:.2f} para {}.'.format(valor, pagamento))
elif forma_pagamento == 2:
    pagamento = 'pagamento à vista no cartão'
    valor = preco - (preco * 5 / 100)
    print('O valor do produto será R${:.2f} para {}.'.format(valor, pagamento))
elif forma_pagamento == 3:
    pagamento = 'pagamento em 2x no cartão'
    valor = preco
    print('O valor do produto será R${:.2f} para {}.'.format(valor, pagamento))
elif forma_pagamento == 4:
    pagamento = 'pagamento em 3x ou mais no cartão'
    valor = preco + (preco * 20 / 100)
    print('O valor do produto será R${:.2f} para {}.'.format(valor, pagamento))
else:
    print('-=' * 20)
    print('Digite uma forma de pagamento válida')
    print('-=' * 20)
    print('Para a forma de pagamento: ')
    print('Digite 1 para pagamento a vista em dinheiro ou cheque.')
    print('Digite 2 para pagamento a vista no cartão.')
    print('Digite 3 para pagamento em 2x no cartão.')
    print('Digite 4 para pagamento em 3x ou mais no cartão.')
    print('-=' * 20)
