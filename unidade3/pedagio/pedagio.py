#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

tipo = (raw_input()) # Tipo de veículo

if tipo == "Automóvel utilitário":
	print "Valor a pagar: R$ 11.40."

elif tipo == "Ônibus":
	eixos = float(raw_input())
	print "Valor a pagar: R$ %.2f." % (eixos * 11.40)

elif tipo == "Caminhão":
	eixos = float(raw_input())
	print "Valor a pagar: R$ %.2f." % (eixos * 9.60)

elif tipo == "Motocicleta":
	print "Valor a pagar: R$ 5.70."

else:
	print "Veículo não cadastrado."
