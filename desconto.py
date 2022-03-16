# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto:'))
desconto = preco * (5/100)
novopreco = preco - desconto
print('Com o desconto de 5% você economiza R$ {:.2f}'.format(desconto))
print('Com o desconto de 5% você pagará apenas R$ {:.2f}'.format(novopreco))
