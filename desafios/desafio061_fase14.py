# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando estrutura while

primeiro_termo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
decimo_termo = primeiro_termo + (10 * razao)
resultado = 1
while primeiro_termo <= decimo_termo:
    primeiro_termo *= razao
    resultado = primeiro_termo
print(resultado)
