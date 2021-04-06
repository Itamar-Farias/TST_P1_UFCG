# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def valor_polinomio():
	somas = []
	while True:
		if polinomio[0] == "fim":
			break
		
		polinomio = raw_input().split()
		valor = float(raw_input())	
		
		for i in range(1, len(polinomio)):
			soma += valor((polinomio[i] * (valor ** i))
		
		somas.append(soma)
		
		print "novo polinomio"
		
		for j in somas:
			print j

valor_polinomio()
