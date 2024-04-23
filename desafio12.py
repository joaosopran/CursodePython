p = float(input('qual é o preço do produto R$: '))
d = p - (p * 5 / 100)
print('o produto que custava R${}, com desconto de 5% passou a custar R$ {:.2f}'.format(p,d))