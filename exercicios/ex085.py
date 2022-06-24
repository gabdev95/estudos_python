# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')