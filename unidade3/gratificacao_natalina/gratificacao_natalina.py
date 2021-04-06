# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

cargo = int(raw_input())
if cargo == 1:
	print "Deverá receber em dezembro R$ 25000.00."
elif cargo == 2:
	print "Deverá receber em dezembro R$ 15000.00."
elif cargo == 3:
	faltas = int(raw_input())
	if faltas == 0:
		print "Valor da gratificação R$ %.2f." % 500.0
		print "Deverá receber em dezembro R$ %.2f." % (8500.0)
	else:
		print "Valor da gratificação R$ %.2f." % ((235 - faltas) * 2.0)
		print "Deverá receber em dezembro R$ %.2f." % (8000.0 + ((235 - faltas) * 2.0))
elif cargo == 4:
	faltas = int(raw_input())
	if faltas == 0:
		print "Valor da gratificação R$ %.2f." % 300.0
		print "Deverá receber em dezembro R$ %.2f." % (5300.0)
	else:
		print "Valor da gratificação R$ %.2f." % ((235 - faltas) * 1.0)
		print "Deverá receber em dezembro R$ %.2f." % (5000.0 + ((235 - faltas) * 1))
else:
	faltas = int(raw_input())
	if faltas == 0:
		print "Valor da gratificação R$ %.2f." % 200.0
		print "Deverá receber em dezembro R$ %.2f." % (3000.0)
	else:
		print "Valor da gratificação R$ %.2f." % ((235 - faltas) * 0.7)
		print "Deverá receber em dezembro R$ %.2f." % (2800.0 + ((235 - faltas) * 0.7))
