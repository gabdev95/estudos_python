# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi algugado. Clacule o preço a pagar,sabendo
# que o carro custa R$60.00 por dia e R$0.15 por km rodado.
km = float(input('Quantos quilometros foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco = (dias * 60) + (km * 0.15)
print('Você percorreu {}km e alugou o carro durante {} dias.'.format(km, dias))
print('O preço que você deverá pagar é de R${:.2f}.'.format(preco))
# {:.2f} duas casa com ponto flutuante
