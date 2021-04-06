#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

a = int(raw_input()) #Quantidade de tweets

pag = a / 400
desperdicio = a % 400
percentual_deperdicio = (100.0 * desperdicio) / a 

print "Serão necessárias %d página(s) para visualizar os tweets." % pag
print "%.1f%% dos tweets serão perdidos." % percentual_deperdicio
