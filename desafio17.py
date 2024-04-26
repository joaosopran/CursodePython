import math

n1 = float(input('Qual comprimento do cateto oposto: '))
n2 = float(input('Qual o comprimento do cateto adjacente: '))

hipo = math.hypot(n1, n2)

print('A hipotenusa vai medir {:.2f}'.format(hipo))