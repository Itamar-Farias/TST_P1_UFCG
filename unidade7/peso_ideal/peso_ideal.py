# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def calcula_peso():
	pesos_ideais = []
	generos = []
	while True:
		dados = raw_input().split()
		if dados[0] == "****":
			break
		elif dados[0] == "m" or dados[0] == "M":
			generos.append("Homem")
			pesos_ideais.append(((72.7 * (float(dados[1]))) - 58.0))
			
		else:
			generos.append("Mulher")
			pesos_ideais.append(((62.1 * (float(dados[1]))) - 44.7))

	for i in range(len(generos)):
		print "%s: peso ideal é %.1f" % (generos[i], pesos_ideais[i])
		
		

calcula_peso()
