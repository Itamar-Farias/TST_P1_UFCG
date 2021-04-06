# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def agrupa_resumos_iguais(lista):
	somas = []
	numeros = []
	for e in lista:
		soma = 0
		numero = str(e)
		for j in range(len(numero)):
			soma += int(numero[j])
		if soma not in  somas:
			somas.append(soma)
		numeros.append(e)
	print somas
	print numeros
	
lista1 = [60, 343, 19, 1230, 51, 123]
assert agrupa_resumos_iguais(lista1) == {6:[60, 1230, 51, 123], 10:[343,19]}
