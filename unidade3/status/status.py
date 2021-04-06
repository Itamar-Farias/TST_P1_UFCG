#coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
quant_faltas = int(raw_input())

media = (nota1 + nota2 + nota3) / 3

if quant_faltas > (30 * 0.25):
	print "reprovado por faltas"
elif quant_faltas < (30 * 0.25) and media < 4:
	print "reprovado por nota"
elif quant_faltas < (30 * 0.25) and (media >= 4 and media < 7):
	print "prova final"
elif quant_faltas < (30 * 0.25) and media >= 7:
	print "aprovado por media"
