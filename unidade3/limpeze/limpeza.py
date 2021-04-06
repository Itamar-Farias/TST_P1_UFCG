# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

servico = int(raw_input())

if servico == 1:
	volume = float(raw_input())
	if volume  * 80 >= 200:
		print "R$ %.f,00" % (volume * 80)
		print "Brinde!"
	else:
		print "R$ %.f,00" % (volume * 80)
elif servico == 2:
	volume = float(raw_input())
	if volume  * 50 >= 200:
		print "R$ %.f,00" % (volume * 50)
		print "Brinde!"
	else:
		print "R$ %.f,00" % (volume * 50)
elif servico == 3:
	print "R$ 50,00"
