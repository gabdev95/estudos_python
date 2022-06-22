# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('''======= MENU =======
[1] somar 
[2] multiplicar 
[3] maior 
[4] novos números 
[5] sair do programa
====================''')
opcao = int(input('Escolha uma opção: '))
opcao4 = True
operacao = 0
maior = 0
while opcao4:
    if opcao == 1:
        opcao4 = False
        operacao = num1 + num2
        print(operacao)
    elif opcao == 2:
        opcao4 = False
        operacao = num1 * num2
        print(operacao)
    elif opcao == 3:
        opcao4 = False
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(maior)
    elif opcao == 4:
        opcao4 = True
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print('''======= MENU =======
[1] somar 
[2] multiplicar 
[3] maior 
[4] novos números 
[5] sair do programa
====================''')
        opcao = int(input('Escolha uma opção: '))
    elif opcao == 5:
        print('Saindo...')
        exit()
