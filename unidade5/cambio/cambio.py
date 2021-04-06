# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

lista_valores = []
lista_convertidos = []
lista_sifra = []
while True:
	conversao = raw_input().split()
	if conversao[0] == "fim":
		break
	elif conversao[0] == "R$" and conversao[3] == "$":
		s = float(conversao[1]) * 2.58 
		lista_valores.append(conversao[1])
		lista_convertidos.append(s)
		lista_sifra.append(conversao[3])
	elif conversao[0] == "R$" and conversao[3] == "€":
		e = float(conversao[1]) * 0.38 
		lista_valores.append(conversao[1])
		lista_convertidos.append(e)
		lista_sifra.append(conversao[3])
	elif conversao[0] == "R$" and conversao[3] == "U$":
		us = float(conversao[1]) * 0.49 
		lista_valores.append(conversao[1])
		lista_convertidos.append(us)
		lista_sifra.append(conversao[3])

for x in range(len(lista_valores)):
	print "R$ %s = %s %.2f" % (lista_valores[x], lista_sifra[x], lista_convertidos[x])
	
