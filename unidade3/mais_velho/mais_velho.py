# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

nome_1 = raw_input()

dia_1 = int(raw_input())
mes_1 = int(raw_input())
ano_1 = int(raw_input())

nome_2 = raw_input()

dia_2 = int(raw_input())
mes_2 = int(raw_input())
ano_2 = int(raw_input())

if ano_1 < ano_2:
	print nome_1

elif ano_1 > ano_2:
	print nome_2

elif ano_1 == ano_2:
	if mes_1 < mes_2:
		print nome_1
	elif mes_1 > mes_2:
		print nome_2
	elif mes_1 == mes_2:
		if dia_1 < dia_2:
			print nome_1
		elif dia_1 > dia_2:
			print nome_2
		else:
			print "nenhuma"
