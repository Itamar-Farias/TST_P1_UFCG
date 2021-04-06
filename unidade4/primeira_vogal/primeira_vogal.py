# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

palavra = raw_input()
lista_vogal = []
for x in range(len(palavra)):
	if palavra[x] in "a,e,i,o,u,A,E,I,O,U":
		print palavra[x]
		lista_vogal.append(palavra[x])
		break

if lista_vogal == []:
	print "-"
