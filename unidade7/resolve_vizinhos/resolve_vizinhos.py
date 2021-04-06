# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def resolve_vizinhos(lista):
	for i in range(len(lista)):
		for j in range(len(lista) - 1):
			if lista[j] == lista[j + 1]:
				lista[j] += 1
			print lista

seq = [1,6,5,5,8,4]
resolve_vizinhos(seq)
print seq
