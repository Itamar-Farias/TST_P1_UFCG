# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def func():
	lista_telefonica = []
	while True:
		nome = raw_input()
		if nome == "####":
			break
		lista_telefonica.append(nome)
		for i in range(len(lista_telefonica)):
			for j in range(len(lista_telefonica) - 1):
				if lista_telefonica[j][0] > lista_telefonica[j + 1][0]:
					lista_telefonica[j], lista_telefonica[j + 1] = lista_telefonica[j + 1], lista_telefonica[j]
		contador = 0
		for k in range(len(lista_telefonica)):
			if lista_telefonica[k] == nome and contador == 0:
				print "* %s" % (lista_telefonica[k])
				contador += 1
			else:
				print lista_telefonica[k]
		print "----"

func()
