#coding: utf-8
#Itamar Farias 115210021
#Programação I

semestres = int(raw_input())
ens = float(raw_input()) # Atividades de ensino
prod_int = float(raw_input()) # Atividades de prod. intelectual
orient = float(raw_input()) # Atividades de orientação
admin = float(raw_input()) # Atividades administrativas
media = ((ens + prod_int + orient + admin) / 4.0) 

if (semestres < 4):
	print "Promoção indeferida. Número de semestres insuficiente."
	
elif (ens < 320) or (prod_int < 100) or (orient < 20):
	print "Promoção indeferida. Pontuação mínima não alcançada."

elif (media < 140):
	print "Promoção indeferida. Média insuficiente."
	
else:
	print "Promoção deferida. Parabéns!"
