# coding: utf-8
# Itamar da Silva Farias	115210021
# programação I


"""Defensivo              volume    preço
   Fungicida	1.0L/ha	    50	     320
   Herbicida	0.3L/ha	    1	     100
   Inseticida	2.5L/ha	    30	     400"""

defensivo = raw_input()
area = float(raw_input())

if defensivo == "Fungicida":
	quantidade = area / 50.0
	
	print "%d Fungicida(s). %.2f reais." % (quantidade, (int(quantidade) * 320))

elif defensivo == "Herbicida":
	quantidade = 0.3 * area
	if quantidade <= 1:
		print "1 Herbicida(s). 100.00 reais."
	else:
		print "%d Herbicida(s). %.2f reais." % (quantidade + 1, ((quantidade + 1.0) * 100))

else:
	quantidade = area / 30
	if quantidade <= 1:
		print "1 Inseticida(s). 400 reais."
	else:
		print "%d Inseticida(s). %.2f reais." % (quantidade + 1, ((int(quantidade) + 1) * 400))
		
