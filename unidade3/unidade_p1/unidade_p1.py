# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

nota = float(raw_input())
numero_miniteste = int(raw_input())
if numero_miniteste == 1:
	print "%.1f. Ainda não aprovado." % nota
elif numero_miniteste != 1:
	nota_1 = float(raw_input())
	media = nota * 0.6 + nota_1 * 0.4
	if media >= 6:
		print "%.1f. Aprovado." % media
	else:
		print "%.1f. Ainda não aprovado." % media
