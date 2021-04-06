# coding: utf -8

quantidade_numeros = int(raw_input())
lista_numero = []
quant_menor_superior0 = 0
quant_maior_superior0 = 0
quant_menor_superior1 = 0
quant_maior_superior1 = 0

for n in range(quantidade_numeros):
	numero = int(raw_input())
	lista_numero.append(numero)

if lista_numero[0] < lista_numero[-1]:
	print "Menor dos extremos: %d" % lista_numero[0]
	
	for x in lista_numero:
		if x < lista_numero[0]:
			quant_menor_superior0 += 1
	
	print "%d número(s) abaixo do menor" % quant_menor_superior0
	
	for x1 in lista_numero:
		if x1 > lista_numero[0]:
			quant_maior_superior0 += 1
			
	print "%d número(s) acima do menor" % quant_maior_superior0
	
elif lista_numero[0] > lista_numero[-1]:
	print "Menor dos extremos: %d" % lista_numero[-1]
	
	for y in lista_numero:
		if y < lista_numero[-1]:
			quant_menor_superior1 += 1
			
	print "%d número(s) abaixo do menor" % quant_menor_superior1
	
	for  y1 in lista_numero:
		if y1 > lista_numero[-1]:
			quant_maior_superior1 += 1
	
	print "%d número(s) acima do menor" % quant_maior_superior1
