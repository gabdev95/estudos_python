# dados = {'nome': 'Pedro', 'idade': 25}
# print(dados['nome'])
# print(dados['idade'])
# print(dados)

# pessoas = {'nome': 'Gabriele', 'sexo': 'M', 'idade': 27}
# print(pessoas['nome'])
# print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.values())
# print(pessoas.keys())
# print(pessoas.items())
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf': 'Pernambuco', 'sigla': 'PE'}
# estado2 = {'uf': 'Paraíba', 'sigla': 'PB'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # copy() cria uma cópia do estado para adicionar outros elementos
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
