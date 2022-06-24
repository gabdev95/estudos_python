# teste = list()
# teste.append('Gabriele')
# teste.append(27)
# galera = list()
# galera.append(teste[:])  # [:] cria uma cópia da lista
# teste[0] = 'João'
# teste[1] = 25
# galera.append(teste[:])  # [:] cria uma cópia da lista
# print(galera)

# galera = [['João', 25], ['Gabriele', 27], ['Slinky', 3], ['Filó', 1]]
# print(galera[0])  # Mostra todos os dados de João
# print(galera[0][0])  # Mostra somente o nome de João
# print(galera[0][1])  # Mostra somente a idade de João
# print(galera[1])  # Mostra todos os dados de Gabriele
# print(galera[1][0])  # Mostra somente o nome de Gabriele
# print(galera[1][1])  # Mostra somente a idade de Gabriele
# print(galera[2])  # Mostra todos os dados de Slinky
# print(galera[2][0])  # Mostra somente o nome de Slinky
# print(galera[2][1])  # Mostra somente a idade de Slinky
# for p in galera:
#     print(f'{p[0]} tem {p[1]} ano(s) de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('-=' * 30)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é MAIOR de idade e tem {p[1]} anos.')
        totmai += 1
    else:
        print(f'{p[0]} é MENOR de idade e tem {p[1]} anos.')
        totmen += 1
print('-=' * 30)
print(f'Temos {totmai} pessoa(s) maior(es) de idade e {totmen} pessoa(s) menor(es) de idade.')
