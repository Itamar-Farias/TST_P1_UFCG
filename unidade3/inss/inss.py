#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

salario = float(raw_input())
c_empregador = salario * 0.12

if (salario <= 1317.07):
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % c_empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % (salario * 0.08)

elif (salario >= 1317.08) and (salario <= 2195.12):
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % c_empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % (salario * 0.09)

else:
	c_empregado = salario * 0.11
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % c_empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % c_empregado
