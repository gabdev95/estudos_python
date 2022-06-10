# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Digite a velocidade do seu carro: '))
valorMulta = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado')
    print('O valor da multa para a velocidade de {}km/h é de R${:.2f}'.format(velocidade, valorMulta))
else:
    print('Velocidade permitida.')
print('Um bom dia e atenção na estrada!')
