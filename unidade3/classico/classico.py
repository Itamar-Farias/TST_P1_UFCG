#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

gols_campinense = int(raw_input())
gols_treze = int(raw_input())

if (gols_campinense > gols_treze):
	print "Campinense"
elif (gols_campinense < gols_treze):
	print "Treze"
else:
	print "Empate"
