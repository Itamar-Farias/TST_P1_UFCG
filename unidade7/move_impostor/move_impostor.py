# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def move_impostor(lista):
	if lista == []:
		return lista
	else:
		for i in range(len(lista)-1):
			if lista[i] != lista[i + 1] - 1:
				lista[i], lista[i + 1] = lista[i + 1], lista[i]
	print lista
lista = [1,2,4,3,5,8]
assert move_impostor(lista) == None
assert lista == [1,2,3,4,5,8]
