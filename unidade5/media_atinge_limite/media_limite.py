# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I

lista_indices = []

while True:
	indice =  raw_input()
	if indice == "-":
		valor_limite = float(raw_input())
		break
	lista_indices.append(float(indice))
	
i = 0
soma = 0
lista_soma = []
lista_i = []
for x in range(len(lista_indices)):
	soma += lista_indices[x] 
	i += 1
	if (soma / i) > valor_limite:
		print "media = %.1f" % (soma / i)
		print "num = %d" % (x+1)
		break

