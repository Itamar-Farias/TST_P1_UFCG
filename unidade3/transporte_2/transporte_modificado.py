# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

quan_pessoas = int(raw_input())
valor = float(raw_input())

if (valor / quan_pessoas)  >= 22 and (valor / quan_pessoas)  < 50:
	print "Ônibus. R$ %.2f" % (quan_pessoas * 22)

elif (valor / quan_pessoas)  >= 22 and (valor / quan_pessoas)  < 100 and quan_pessoas > 4:
	print "Ônibus. R$ %.2f" % (quan_pessoas * 22)

elif (valor / quan_pessoas)  >= 100:
	print "TAV. R$ %.2f" % (quan_pessoas * 100)

elif (valor / quan_pessoas)  >= 50 and (valor / quan_pessoas)  < 100 and quan_pessoas <= 4:
	print "Táxi. R$ %.2f" % 200

elif (valor / quan_pessoas)  < 22:
	print "Não é possível realizar a viagem." 
