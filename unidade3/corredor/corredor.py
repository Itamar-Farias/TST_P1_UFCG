#coding: utf-8
#Itamar Farias 115210021
#Programação I

distancia = float(raw_input())
tempo = float(raw_input())
velocidade = distancia / tempo
print "Distância?Tempo?"
if (velocidade < 10.0):
	print "Velocidade: %.1fkm/h. Corredor amador." % velocidade
elif (velocidade >= 10.0) and (velocidade < 15.0):
	print "Velocidade: %.1fkm/h. Corredor aspirante." % velocidade
elif velocidade == 15:
	print "Velocidade: %.1fkm/h. Corredor aspirante." % velocidade
elif velocidade > 15:
	print "Velocidade: %.1fkm/h. Corredor profissional." % velocidade
	
