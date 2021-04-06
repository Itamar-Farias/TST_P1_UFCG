# coding: utf-8
# Itamar da Silva Farias	115210021
# programação I

def insere_na_fila(fila, nome, altura):
	for i in range(len(fila)):
		if i == 0:
			if altura < fila[i][1]:
				fila.insert(i, (nome, altura))
				break
		elif altura > fila[i-1][1] and altura < fila[i][1]:
			fila.insert(i, (nome, altura))
			break
		elif i == len(fila)-1:
			if altura > fila[i][1]:
				fila.insert(i+1, (nome, altura))
				break

