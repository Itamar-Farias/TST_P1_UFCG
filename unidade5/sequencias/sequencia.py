#coding: utf-8
#Itamar Farias 115210021
#Programação I

print "Mastery Learning"
print "Cálculo da nota na unidade"
print
while True:
	nota_1 = float(raw_input("Nota? "))
	nota_2 = float(raw_input("Nota? "))
	media = (nota_1 + nota_2) / 2
	if media >= 7.0: break
	print "Média: %.1f (cursando)"
