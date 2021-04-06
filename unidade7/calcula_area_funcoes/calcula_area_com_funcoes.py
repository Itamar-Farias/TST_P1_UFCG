# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def areas():
	resultados = []
	import math
	while True:
		poligno = raw_input().split()
		if poligno[0] == "fim":
			break
		
		elif poligno[0] == "Q":
			area = float(poligno[1]) ** 2
			print  "A área do quadrado é %.2f" % area
		
		elif poligno[0] == "C":
			area  = math.pi * (float(poligno[1]) ** 2)
			print "A área do círculo é %.2f" % area
		
		else:
			area = (float(poligno[1]) * float(poligno[2])) / 2
			print "A área do triangulo é %.2f" % area

areas()
