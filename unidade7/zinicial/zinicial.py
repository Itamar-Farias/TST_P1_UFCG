# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def z_inicial(lista):
	quantidades_de_z = 0
	for i in range(len(lista)):
		if lista[i][0] == "z" or lista[i][0] == "Z":
			quantidades_de_z += 1
	
	return quantidades_de_z

lista = raw_input().split()
print z_inicial(lista)
