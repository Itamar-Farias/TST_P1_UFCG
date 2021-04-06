# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def bubblesort(dados):
	while True:
		troca = False
		for i in range(0, len(dados)-1):
			if dados[i] > dados[i+1]:
				dados[i], dados[i+1] = dados[i+1], dados[i]
				troca = True
		if not troca: break	
	return dados
