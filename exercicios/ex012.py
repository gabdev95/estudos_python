# Faça um algoritmo que leia o preço de um produto e mostra seu novo preço com 5% de desconto
preco = float(input('Digite o preço do produto: R$'))
novo = preco - (preco*5/100)
print('O preço do produto, que era R${:.2f}, fica R${:.2f} com o desconto de 5%'.format(preco, novo))
# formatação para ficar com 2 pontos flutuantes {:.2f}
