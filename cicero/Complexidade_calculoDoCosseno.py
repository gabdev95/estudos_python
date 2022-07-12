# Complexidade – Cálculo do cosseno através de uma série de valores com o
# fatorial

def fatorial(entrada):
    if entrada <= 1:
        return 1
    else:
        return entrada * fatorial(entrada - 1)


def exponencial(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * exponencial(base, expoente - 1)


def interacao(n, x):  # equação dada para o cálculo do cosseno
    return exponencial(-1, n) / fatorial(2 * n) * exponencial(x, 2 * n)


def calcula_cosseno(x):
    cosx = 0
    for n in range(50):  # loop de interações
        cosx += interacao(n, x)  # incrementa o cosseno dentro das interações
    return cosx


x = float(input(''))
print(f'{calcula_cosseno(x):.4f}')
