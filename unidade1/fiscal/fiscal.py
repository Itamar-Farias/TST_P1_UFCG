#coding: utf-8
valor_total = float(raw_input())
data = raw_input()
quantidade_de_produtos = float(raw_input())

media = valor_total / quantidade_de_produtos
print 'Data: %s' % data
print 'O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de R$ %.1f.\n' % (valor_total, media)

