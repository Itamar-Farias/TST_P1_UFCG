# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

print "Mastery Learning"
print "Cálculo da nota na unidade"
print

media = 0.0
media_atual = 0.0
penalizacao = 0.0

nota_1 = float(raw_input("Nota? "))
nota_2 =  float(raw_input("Nota? "))
media = (nota_1 + nota_2) / 2

if nota_1 < nota_2:
	transicao = nota_1
	nota_1 = nota_2
	nota_2 = transicao
if media < 6.0:
	print "Média: %.1f (cursando)" % media	
else:
	print "Média: %.1f (aprovado)" % media
print "Penalização: %.1f" % penalizacao
print

while media < 6.0:
	penalizacao += 0.5
	auxiliar = float(raw_input("Nota? "))
	if nota_2 < auxiliar:
		nota_2 = auxiliar
	
	if nota_1 < nota_2:
		transicao = nota_1
		nota_1 = nota_2
		nota_2 = transicao
	
	media = (nota_1 + nota_2) / 2
	if media < 6.0:
		print "Média: %.1f (cursando)" % media	
	else:
		print "Média: %.1f (aprovado)" % media
	print "Penalização: %.1f" % penalizacao
	print
	
print "==="
print "Notas válidas: %.1f e %.1f" % (nota_1, nota_2)
print "Média parcial na unidade: %.1f" % media
print "Penalizações: %.1f" % penalizacao
print "Média final na unidade: %.1f" % (media - penalizacao)
