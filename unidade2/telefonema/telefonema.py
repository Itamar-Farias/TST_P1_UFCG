# coding: utf-8
# Itamar da Silva Farias	1115210021
# Programação I

tempo = int(raw_input())
valor = 0
if tempo <= 3:
	valor += tempo * 0.5 + 1
elif tempo % 10 == 8 or tempo % 10 == 3:
	valor += tempo  * 5
else:
	valor += tempo * 0.7
	
print "R$ %.2f" % (valor)
