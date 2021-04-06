# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

import random
numero = random.randint(0,1000)
tentativas  = 0

while True:
	palpite = int(raw_input("palpite? "))
	tentativas += 1
	if palpite < numero:
		print "baixo"
	elif palpite > numero:
		print "alto"
	elif palpite == numero:
		print "Você acertou em %d tentativas." % tentativas
		break
		
