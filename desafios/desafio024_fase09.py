# Crie um programa que leia o nome de um local e diga se começa
# ou não com o nome Santo

local = str(input('Escreva o nome do lugar onde você mora: ')).strip()
lista = local.lower().split()
pnome = lista[0]
if pnome == 'santo':
    print('O nome do local onde você mora começa com "Santo".')

else:
    print('O nome do local onde você mora não começa com "Santo".')
