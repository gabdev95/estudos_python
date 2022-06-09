local = str(input('Escreva o nome do lugar onde você mora: '))
lista = local.lower().split()
pnome = lista[0]
if pnome == 'santo':
    print('O nome do local onde você mora começa com "Santo".')

else:
    print('O nome do local onde você mora não começa com "Santo".')
