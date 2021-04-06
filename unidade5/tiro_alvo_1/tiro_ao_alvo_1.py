# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

lista_distancia = []
soma = 0

while True:
	ponto = raw_input().split(",")
	dist = (((float(ponto[0])) ** 2) + ((float(ponto[1]) ** 2))) ** 0.5
	if dist > 200: 	
		break
	lista_distancia.append(dist)
	soma += dist

for x in lista_distancia:
	print "%.2f" % x

print "--"
print "num disparos: %d" % len(lista_distancia)
print "distancia media: %.2f" % (soma / len(lista_distancia)) 
