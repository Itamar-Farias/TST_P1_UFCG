# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def encontra_menores(num, lista):
	contador = 0
	for i in range(len(lista)):
		if int(lista[i]) <  num:
			return int(lista[i])
	if contador == 0:
		return -1
