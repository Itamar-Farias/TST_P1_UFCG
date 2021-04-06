# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação 

soma = 0
quant_numeros = 0
posicao = 1
lista_posicao = []
lista_numero = []

while soma < 100:
	numero = float(raw_input())
	lista_numero.append(numero)
	quant_numeros += 1
	lista_posicao.append(posicao)
	posicao += 1
	soma += numero
	
print "Quantidade de números lidos: %d" % quant_numeros
print "Soma dos números lidos: %.2f" % soma

media = (soma / quant_numeros)
print  "Média = %.2f" % media
print 
print "Abaixo da média"
for x in range(len(lista_numero)):
	if lista_numero[x] < media:
		print "%.2f (%do)" % (lista_numero[x], lista_posicao[x])
print 
print "Acima da média"
for y in range(len(lista_numero)):
	if lista_numero[y] > media:
		print "%.2f (%do)" % (lista_numero[y], lista_posicao[y])	
