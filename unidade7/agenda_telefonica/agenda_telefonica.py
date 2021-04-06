# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

nomes_numeros = []

def insere(nome,numero):
	if len(nomes_numeros) < 1:
		nomes_numeros.append((nome,numero))
	else:
		nomes_numeros.append((nome,numero))
		for i in range(len(nomes_numeros)):
			for j in range(len(nomes_numeros)-1-i):
				if nomes_numeros[j][0] > nomes_numeros[j+1][0]:
					nomes_numeros[j],nomes_numeros[j+1] = nomes_numeros[j+1], nomes_numeros[j]
					
def imprime():
	for i in nomes_numeros:
		print "Nome: %s" % i[0]
		print "Fone: %s" % i[1]
		print "----------"
		
def busca(nome):
	achou = False
	for i in nomes_numeros:
		if nome == i[0]:
			print "Nome: %s" % i[0]
			print "Fone: %s" % i[1]
			print "----------"
			achou = True
	if achou == False:
		print "Nome inexistente"
		print "----------"

while True:
	seq = raw_input()
	if seq == "finalizar": 
		break
	if seq == "inserir":
		num = int(raw_input())
		for i in range(num):
			nome = raw_input()
			numero = raw_input()
			insere(nome,numero)
	elif seq == "buscar":
		nome = raw_input()
		busca(nome)
	elif seq == "imprimir":
		imprime()
