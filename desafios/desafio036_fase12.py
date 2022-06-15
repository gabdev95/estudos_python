# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não deve exceder 30% do salário,
# ou então o empréstimo será negado

valor_casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário mensal? R$'))
anos = int(input('Em quantos anos inteiros você pretende pagar o financiamento? '))
mensalidade_ate = (salario * 30 / 100)
meses = anos * 12
parcelas = valor_casa / meses
if parcelas <= mensalidade_ate:
    print('Empréstimo aprovado! Suas parcelas serão de R${:.2f}.'.format(parcelas))
else:
    print('Empréstimo NEGADO!')
