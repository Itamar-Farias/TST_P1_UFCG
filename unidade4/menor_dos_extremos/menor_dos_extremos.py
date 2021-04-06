# coding: utf -8
# Itamar da Silva Farias
# Programação I

quantidade_inteiros = int(raw_input())
lista_numeros = []
total_numeros = 0


for n in range(quantidade_inteiros): #
	numero = int(raw_input())
	lista_numeros.append(numero)
	total_numeros += 1

quant_numeros_menor_extremo0 = 0
quant_numeros_maior_extremo0 = 0

if lista_numeros[0] < lista_numeros[-1]:
	print "Menor dos extremos: %d" % lista_numeros[0]
	
	for x in lista_numeros:
		if x < lista_numeros[0]:
			quant_numeros_menor_extremo0 += 1
		if x > lista_numeros[0]:
			quant_numeros_maior_extremo0 += 1
			
	print "%d número(s) abaixo do menor" % quant_numeros_menor_extremo0
	print "%d número(s) acima do menor" % quant_numeros_maior_extremo0
	
quant_numeros_menor_extremo1 = 0
quant_numeros_maior_extremo1 = 0

if lista_numeros[0] > lista_numeros[-1]:
	print "Menor dos extremos: %d" % lista_numeros[-1]
	
	for x1 in lista_numeros:
		if x1 < lista_numeros[-1]:
			quant_numeros_menor_extremo1 += 1
		if x1 > lista_numeros[-1]:
			quant_numeros_maior_extremo1 += 1
	
	print "%d número(s) abaixo do menor" % quant_numeros_menor_extremo1
	print "%d número(s) acima do menor" % quant_numeros_maior_extremo1
			
quant_numeros_menor_extremo2 = 0	
quant_numeros_maior_extremo2 = 0

if lista_numeros[0] == lista_numeros[-1]:
	print "Menor dos extremos: %d" % lista_numeros[-1]
	
	for x2 in lista_numeros:
		if x2 < lista_numeros[-1]:
			quant_numeros_menor_extremo2 += 1
		if x2 > lista_numeros[-1]:
			quant_numeros_maior_extremo2 += 1
	
	print "%d número(s) abaixo do menor" % quant_numeros_menor_extremo2
	print "%d número(s) acima do menor" % quant_numeros_maior_extremo2
