# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def triangulo_Pascal(n):
    triangulo = [[1],[1,1]]
    for i in range(1,n):
        linha = [1]
        for j in range(0,len(triangulo[i])-1):
            linha += [triangulo[i][j] + triangulo[i][j+1]]
        linha += [1]
        triangulo += [linha]
    return triangulo

n = int(raw_input())
if n >= 2:
	resultado = triangulo_Pascal(n - 1)

	somas = []
	for k in resultado:
		lista_final = []
		for x in range(len(k)):
			lista_final.append(str(k[x]))
		print " ".join(lista_final)
		soma = 0
		for l in range(len(k)):
			soma += int(k[l])
		somas.append(soma)

	for m in somas:
		print m
		
elif n == 0:
	print "1"
	print "1"

elif n == 1:
	print "1"
	print "1 1"
	print "1"
	print "2" 
