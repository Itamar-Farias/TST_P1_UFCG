#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

angulo = float(raw_input())
resto = angulo % 360
if angulo == 0:
	print "Sobre eixos"
if angulo <= 360 and angulo != 0:
	if 90 / angulo > 1:
		print "Quadrante 1"
	elif 90 / angulo == 1:
		print "Sobre eixos"
	elif 180 / angulo > 1:
		print "Quadrante 2"
	elif 180 / angulo == 1:
		print "Sobre eixos"
	elif 270 / angulo > 1:
		print "Quadrante 3"
	elif 270 / angulo == 1:
		print "Sobre eixos"
	elif 360 / angulo > 1:
		print "Quadrante 4"
	elif 360 / angulo == 1:
		print "Sobre eixos"

elif angulo > 360:
	if 90 / resto > 1:
		print "Quadrante 1"
	elif 90 / resto == 1:
		print "Sobre eixos"
	elif 180 / resto > 1:
		print "Quadrante 2"
	elif 180 / resto == 1:
		print "Sobre eixos"
	elif 270 / resto > 1:
		print "Quadrante 3"
	elif 270 / resto == 1:
		print "Sobre eixos"
	elif 360 / resto > 1:
		print "Quadrante 4"
	elif 360 / resto == 1:
		print "Sobre eixos"			 
