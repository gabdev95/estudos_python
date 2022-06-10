# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200km e
# R$0,45 para viagens mais longas.

distancia = float(input('Digite a distância em quilômetros: '))
if distancia <= 200:
    print('A passagem vai custar R${:.2f}.'.format(distancia * 0.50))
else:
    print('A passagem vai custar R${:.2f}.'.format(distancia * 0.45))