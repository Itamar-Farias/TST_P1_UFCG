# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def ordenar_pacientes():
	pacientes = []
	while True:
		paciente = raw_input().split()
		if paciente[0] == "fim":
			break
		pacientes.append(paciente)

	vermelhos = 0
	laranjas = 0
	amarelos = 0
	verdes = 0
	azuis = 0

	lista_vermelho = []
	lista_laranja = []
	lista_amarelo = []
	lista_verde = []
	lista_azul = []

	for i in range(len(pacientes)):
		if pacientes[i][1] == "vermelho":
			vermelhos += 1
			lista_vermelho.append(pacientes[i][0])
		elif pacientes[i][1] == "laranja":
			laranjas += 1
			lista_laranja.append(pacientes[i][0])
		elif pacientes[i][1] == "amarelo":
			amarelos += 1
			lista_amarelo.append(pacientes[i][0])
		elif pacientes[i][1] == "verde":
			verdes += 1
			lista_verde.append(pacientes[i][0])
		else:
			azuis += 1
			lista_azul.append(pacientes[i][0])

	for j in lista_vermelho:
		print j
	for k in lista_laranja:
		print k
	for l in lista_amarelo:
		print l
	for m in lista_verde:
		print m
	for n in lista_azul:
		print n

	print "---"
	print "vermelho: %d" % vermelhos
	print "laranja: %d" % laranjas
	print "amarelo: %d" % amarelos
	print "verde: %d" % verdes
	print "azul: %d" % azuis
	print "---" 

ordenar_pacientes()
