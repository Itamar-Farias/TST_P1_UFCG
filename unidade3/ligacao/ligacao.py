#coding: utf-8
#Itamar Farias 115210021
#Programação I

tempo = int(raw_input())
taxa = 1.0
valor = 0.0

if tempo <= 3:
	print "R$ %.2f" % (taxa + tempo * 0.5)

else:
	x = tempo / 5
	valor += x * 3.0
	y = tempo % 5
	valor += y * 0.70
	print "R$ %.2f" % (valor + taxa)
