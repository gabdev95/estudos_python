# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort()  # Mostra num em ordem númerica. Para inverter -> num.sort(reverse=True)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 5 in num:
#    num.remove(5)
# else:
#     print('Não achei o número 5')
# num.remove(2)  # elimina o primeiro elemento encontrado
# num.pop()  # apagou último elemento
# num.pop(2)  # apagou o elemento do índice 2
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

# valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei {v}!')
# print('Cheguei ao final da lista.')

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei {v}!')
# print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:]  # b recebe todos os valores de a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
