# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

s = 0
media_idade = 0
maior_idade_masc = 0
quantidade_mulheres = 0
lista_idades = []
lista_nomes = []
pos_idade = 0
for pessoas in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoas))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoas)))
    sexo = str(input('Digite o sexo da {}ª pessoa: '.format(pessoas))).strip().upper()
    s += idade
    media_idade = s / 4
    if sexo == 'MASCULINO':
        lista_idades.append(idade)
        lista_nomes.append(nome)
        maior_idade_masc = max(lista_idades, key=int)
        pos_idade = lista_idades.index(maior_idade_masc)
    else:
        if idade < 20:
            quantidade_mulheres += 1
print('-=' * 20)
print('A média de idade do grupo é: {} anos.'.format(media_idade))
print('O homem mais velho do grupo se chama {} e tem {} anos.'.format(lista_nomes[pos_idade], maior_idade_masc))
print('Existem {} mulher(es) com idade menor que 20 anos.'.format(quantidade_mulheres))
print('-=' * 20)
