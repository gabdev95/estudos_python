# Crie um programa que leia o nome de um local e diga se começa
# ou não com o nome Santo

local = str(input('Digite o nome do local onde você mora: ')).strip()
print(local[:5].upper() == 'SANTO')
