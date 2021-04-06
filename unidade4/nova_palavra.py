# coding: utf-8
# Itamar da Silva Farias	115210021	 
# Programção I

nome = raw_input()
numero = raw_input()
nova_palavra = ""
n = 1
for x in range(len(nome)):
	nova_palavra += (nome[x] * (int(numero[-1]) + n)) 
	n += -1

print nova_palavra
