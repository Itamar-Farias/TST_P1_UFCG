# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

numero_alvo = int(raw_input())
ordem = 0
while True:
	ordem += 1
	quant_maiores = 0
	numero = raw_input().split()
	x = numero[0]
	if x == "fim":
		break
	for i in range(len(numero)):
		if int(numero[i]) > numero_alvo:
			quant_maiores += 1
	if quant_maiores > len(numero) / 2:
		print "sequencia %d: %s" % (ordem, " ".join(numero))
			
