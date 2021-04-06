# coding: utf-8
# Itamar da Silva Farias	115210021
# programação I

lista = []
soma = 0

while True:
	valor = raw_input()
	if valor == "fim": break
	lista.append(int(valor))
	soma += int(valor)
	
media = float(soma) / len(lista)

print "%.2f" % media

for i in range(len(lista)):
	if lista[i] < media: print "%d %d" % (i+1, lista[i])
