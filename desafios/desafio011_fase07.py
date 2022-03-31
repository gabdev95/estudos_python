larg = float(input('Qual é a largura, em metros, da parede que será pintada? '))
alt = float(input('Qual é a altura, em metros, da parede que será pintada? '))
area = float(larg*alt)
print('Sua parede tem {}m².\nPara pintá-la, serão necessários {}l de tinta.'.format(area, area/2))
