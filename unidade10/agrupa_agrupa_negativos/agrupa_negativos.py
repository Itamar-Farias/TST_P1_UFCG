# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def  agrupa_negativos(lista):
	negativos = []
	nao_negativos = []
	for e in lista:
		if e < 0:
			negativos.append(e)
		else:
			nao_negativos.append(e)
	
	dicionario = {"nao-negativos": nao_negativos, "negativos": negativos}
	return dicionario
