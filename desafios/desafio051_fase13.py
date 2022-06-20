# Desenvolva um programa que leia o primeiro termo e a razão de uma
# progressão aritmética. No final, mostre os 10 primeiro termos dessa progressão

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
decimo_termo = primeiro_termo + (10 * razao)
for c in range(primeiro_termo, decimo_termo, razao):
    print(c)
