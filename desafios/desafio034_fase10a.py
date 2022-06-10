# Escreva um progrma que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a
# R$ 1250.00, calcule um aumento de 10%. Para inferiores ou iguais,
# o aumento é de 15%

salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    novoSalario = salario + ((salario * 10) / 100)
    print('O novo salário do funcionário será de R${:.2f}.'.format(novoSalario))
else:
    novoSalario = salario + ((salario * 15) / 100)
    print('O novo salário do funcionário será de R${:.2f}.'.format(novoSalario))
