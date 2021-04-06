# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def ultimo_indice(num, lista):
	for i in range(len(lista)-1, -1, -1):
		if lista[i] == num:
			return i
	
	return -1
