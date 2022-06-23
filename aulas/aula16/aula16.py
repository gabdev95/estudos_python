'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(lanche[3])  # Mostra o índice 3 (pudim) da tupla

print(sorted(lanche))  # Em ordem alfabética

for comidas in lanche:
    print(f'Eu vou come {comidas}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))
print(c)
print(c.count(5))
print(c.index(8))'''

pessoa = ('Gabriele', 27, 'F', 49.2)
# del(pessoa) apaga a tupla inteira
print(pessoa)
