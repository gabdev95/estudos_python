# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))
imc = peso / (altura ** 2)
print('Tendo {:.2f}m de altura e {:.1f}kg de peso'.format(altura, peso))
print('-=' * 20)
print('Seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL')
elif 18.5 < imc < 25:
    print('Você está no PESO IDEAL')
elif 25 < imc < 30:
    print('Você está com SOBREPESO')
elif 30 < imc < 40:
    print('Você está OBESO')
else:
    print('Você está com OBESIDADE MÓRBIDA')
print('-=' * 20)
