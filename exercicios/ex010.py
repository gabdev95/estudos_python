# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere o dólar = R$3,27
real = float(input('Quantos Reais você tem na sua carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f}, você pode comprar US${:.2f}.'.format(real, dolar))
# :.2f serve pra deixar dois pontos flutuantes
