preco = float(input('Qual é o preço atual do produto? '))
desc = float((preco*5)/100)
print('O valor sem desconto é: {};\nCom desconto fica: {}.'.format(preco, preco-desc))
