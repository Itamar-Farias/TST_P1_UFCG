# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

nota_a = float(raw_input())
nota_b = float(raw_input())
nota_c = float(raw_input())
idade_candidato_1 = int(raw_input())
nota_1 = float(raw_input())
nota_2 = float(raw_input())
nota_3 = float(raw_input())
idade_candidato_2 = int(raw_input())

media_1 = nota_a * 0.3 + nota_b * 0.4 + nota_c * 0.3
media_2 = nota_1 * 0.3 + nota_2 * 0.4 + nota_3 * 0.3

if media_1 > media_2:
	print "O primeiro candidato foi aprovado com média %.1f." % media_1
elif media_1 < media_2:
	print "O segundo candidato foi aprovado com média %.1f." % media_2

else: 
	if idade_candidato_1 > idade_candidato_2:
		print "O primeiro candidato foi aprovado com média %.1f." % media_1
	elif idade_candidato_1 < idade_candidato_2:
		print "O segundo candidato foi aprovado com média %.1f." % media_2
	else:
		print "Empate."	
