nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Gabriele':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem comum!')
print('Tenha um bom dia, {}!'.format(nome))

