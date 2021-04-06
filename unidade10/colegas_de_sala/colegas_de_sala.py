# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def colegas_de_sala(salasprofs, professor):
	colegas_de_sala = []
	sala = salasprofs[professor]
	for i in salasprofs:
		if i != professor and salasprofs[i] == sala:
			colegas_de_sala.append(i)
	return colegas_de_sala
