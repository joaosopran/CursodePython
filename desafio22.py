nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
