# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

lista_distancia = []
melhor_tiro = 200
soma = 0
while True:
	x = float(raw_input())
	y = float(raw_input())
	dist = (((x - 0) ** 2) + ((y - 0) ** 2)) ** 0.5
	if dist >= 200: 	
		break
	lista_distancia.append(dist)
	soma += dist
	if melhor_tiro > dist:
		melhor_tiro = dist
		print "%.2f cm (melhor tiro)" % melhor_tiro
	else:
		print "%.2f cm" % dist

print "--"
print "num tiros: %d" % len(lista_distancia)
print "melhor tiro: %.2f cm" % melhor_tiro
print "distancia media: %.2f cm" % (soma / len(lista_distancia)) 
