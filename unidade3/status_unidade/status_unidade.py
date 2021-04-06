# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

numero_mtp = int(raw_input())

if numero_mtp == 1:
	nota_1 = float(raw_input())
	print nota_1
	print "Aluno ainda não aprovado na unidade"

elif numero_mtp == 2:
	nota_1 = float(raw_input())
	nota_2 = float(raw_input()) 
	media = (nota_1 + nota_2) / 2
	if media < 6.0:
		print media - 0.5
		print "Aluno ainda não aprovado na unidade"
	else:
		print media
		print "Aluno aprovado na unidade"

elif numero_mtp == 3:
	nota_1 = float(raw_input())
	nota_2 = float(raw_input()) 
	nota_3 = float(raw_input())
	media = (nota_1 + nota_2 + nota_3) / 3
	if media < 6.0:
		print media - 0.5
		print "Aluno ainda não aprovado na unidade"
	else:
		print media
		print "Aluno aprovado na unidade"

elif numero_mtp == 4:
	nota_1 = float(raw_input())
	nota_2 = float(raw_input())
	nota_3 = float(raw_input())
	nota_4 = float(raw_input()) 
	media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
	if media < 6.0:
		print media - 0.5
		print "Aluno ainda não aprovado na unidade"
	else:
		print media
		print "Aluno aprovado na unidade"
