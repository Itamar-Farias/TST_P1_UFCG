#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

angulo = float(raw_input())
resto = int(angulo) % 360

if (int(angulo < 360)):
	if (int(angulo > 0)) and (int(angulo < 90)):
		print "Quadrante 1" 
	elif (int(angulo > 90)) and (int(angulo < 180)):
		print "Quadrante 2" 
	elif (int(angulo > 180)) and (int(angulo < 270)):
		print "Quadrante 3" 
	elif (int(angulo > 270)) and (int(angulo < 360)):
		print "Quadrante 4"
	elif (angulo == 0) or (angulo == 90) or (angulo == 270) or (angulo == 360):
		print "Sobre eixos"
	
elif ((int(angulo > 360))): 
	if (resto > 0) and (resto < 90):
		print "Quadrante 1" 
	elif (resto > 90) and (resto < 180):
		print "Quadrante 2" 
	elif (resto > 180) and (resto < 270):
		print "Quadrante 3" 
	elif (resto > 270) and (resto < 360):
		print "Quadrante 4"
	elif (resto == 0) or (resto == 90) or (resto == 270) or (resto == 360):
		print "Sobre eixos"

