# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def disciplinas(alocacao, professor):
	
	disciplinas = []
	creditos = 0
	
	for key in alocacao:
		for j in alocacao[key]:
			if professor == j:
				disciplinas.append(key[0])
				creditos += key[1]
	
	return (disciplinas,creditos)
