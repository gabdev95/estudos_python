# Crie um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para píntá-la, sabendo que cada
# litro de tinta pinta uma área de 2m²
larg = float(input('Digite a largura, em metros, da parede: '))
alt = (float(input('Digite a altura, em metros, da parede: ')))
area = larg*alt
print('Sua parede tem a dimensão de {}x{}m e a área é de {}m².'.format(larg, alt, area))
tinta = area/2
print('Para pintá-la, serão necessários {}l de tinta.'.format(tinta))
