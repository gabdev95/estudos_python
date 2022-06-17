# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uam mensagem final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))
if 5 <= media < 7:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')
