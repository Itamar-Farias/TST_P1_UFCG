# coding: utf-8
# Itamar da Silva Farias	115210021
# programação I

soma = 0
lista_geral = []
while True:
	nome = raw_input()
	if nome == "**": break
	if nome != "**":
		while True:
			nota = raw_input()
			if nota == "*": break
			soma += float(nota)
	
print "Relatório de novas questões:"


