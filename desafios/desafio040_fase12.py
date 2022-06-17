# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uam mensagem final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a nota da primeira unidade do aluno: '))
nota2 = float(input('Digite a nota da segunda unidade do aluno: '))
media = (nota1 + nota2) / 2
print('A média do aluno é {:.1f}.'.format(media))
if media < 5:
    print('Média abaixo de 5.0. Aluno REPROVADO')
elif 5 <= media < 7:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno APROVADO')
