frase = 'Curso em Vídeo Python'
frase2 = '   Curso em Vídeo Python'
print(frase)
print(frase[3])  # mostra a letra que está no espaço 3 da frase
print(frase[3:14])  # mostra as letras que estão entre os espaços 3 e 14, mas ignora a letra do espaço 14
print(frase[:14])  # mostra as letras do início ao espaço 14
print(frase[14:])  # mostra as letras do espaço 14 ao final
print(frase[1:14:2])  # mostra as letras que estão entre os espaços 3 e 14, pulando de 2 em 2
print(frase[::2])  # mostra as letras do início ao final, pulando de 2 em 2
print(len(frase))  # conta o comprimento da frase
print(frase.count('o'))  # conta quantas vezes o 'o' minusculo aparece
print(frase.count('O'))  # conta quantas vezes o 'O' maiusculo aparece
print(frase.upper().count('O'))  # transformas todas as letras em maiusculas e conta os 'O'
print(len(frase2.strip()))  # não conta os espaços antes e depois
print(frase.replace('Python', 'Android'))  # Troca 'Python' por 'Android'
print('Curso' in frase)  # Mostra se a palavra 'Curso' está na frase
print(frase.lower().find('vídeo'))  # torna a frase para minusc. e procura a palavra 'vídeo'
print(frase.split())  # mostra as palavras da frase
