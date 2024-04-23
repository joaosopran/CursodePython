sal = float(input('Valor do salário do funcionário R$: '))
aum = sal + (sal * 15 / 100)

print('o salário era de R$ {:.2f}, com aumento de 15% passou a ser de R$ {:.2f}'.format(sal,aum))