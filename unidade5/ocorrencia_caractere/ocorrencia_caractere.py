# coding: utf-8
# Itamar da Silva Farias	1115210021
# Programação I

palavra = raw_input()
conj_palavras = []

while palavra != "fim":
	palavra = raw_input()
	conj_palavras.append(palavra)
numero_letras = []
if conj_palavras == []:
	print "Nenhuma palavra encontrada."
elif conj_palavras != []:
	c = raw_input()
	n = int(raw_input())
	for x in range(len(conj_palavras)):
		for y in range(len(conj_palavras[x])):
			if conj_palavras[x][y] == c and c > n:
				numero_letras.append(conj_palavras[x])

print numero_letras
