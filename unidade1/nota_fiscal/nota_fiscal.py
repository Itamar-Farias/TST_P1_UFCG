# coding: utf-8
# Itamar da Silva Farias 115210021	
# Programação I

valor_total = float(raw_input())
data = raw_input()
quantidade_de_produtos = int(raw_input())

media = valor_total / quantidade_de_produtos
print 'Data: %s' % data
print 'O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f.' % (valor_total, media)
