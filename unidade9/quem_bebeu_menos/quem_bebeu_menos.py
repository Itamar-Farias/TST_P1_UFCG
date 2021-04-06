# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def quem_bebeu_mais_menos(sabado, domingo):

	lista = [0] * len(sabado)
	for i in range(len(sabado)):
		for j in range(len(sabado[i])):
			lista[j] += sabado[i][j]

	for k in range(len(domingo)):
		for z in range(len(domingo[k])):
			lista[z] += domingo[k][z]

	maior_num = lista[0]
	menor_num = lista[0]
	menor = 0
	maior = 0


	for m in range(len(lista)):
		if lista[m] <= menor_num:
			menor_num = lista[m]
			menor = m
		elif lista[m] >= maior_num:
			maior_num = lista[m]
			maior = m
		
	maior += 1
	menor += 1

	return (maior,menor)

sabado = [[1,2,3], [0,1,0], [3,1,2]]
domingo = [[2,1,3], [0,2,1], [1,1,2]]
assert quem_bebeu_mais_menos(sabado, domingo) == (3,1)
sabado = [[1,2,3,4,5], [0,1,2,3,1], [2,1,0,1,2], [3,1,2,1,3], [4,1,3,0,0]]
domingo = [[0,1,1,0,1], [1,2,2,0,2], [2,3,1,1,1], [3,4,2,0,0], [4,3,3,0,0]]
assert quem_bebeu_mais_menos(sabado, domingo) == (1,4)


 
