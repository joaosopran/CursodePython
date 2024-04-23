dia = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos quilometros rodados com o carro: '))

preco = (dia * 60) + (km * 0.15)

print('o total a pagar é de R$ {:.2f}'.format(preco))