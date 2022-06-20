# Desenvolva um programa que leia o primeiro termo e a razão de uma
# progressão aritmética. No final, mostre os 10 primeiro termos dessa progressão

primeiro = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 * razao)
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')

