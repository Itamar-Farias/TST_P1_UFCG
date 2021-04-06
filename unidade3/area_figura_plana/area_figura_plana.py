# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

figura = raw_input()

if figura == "triângulo":
	base = float(raw_input())
	altura = float(raw_input())
	area = (base * altura) / 2
	print "Área do triângulo: %.2f (cm2)" % area 

elif figura == "retângulo":
	base = float(raw_input())
	altura = float(raw_input())
	area = base * altura
	print "Área do retângulo: %.2f (cm2)" % area 

elif figura == "quadrado":
	lado = float(raw_input())
	area = lado ** 2
	print "Área do quadrado: %.2f (cm2)" % area 

else:
	import math
	raio = float(raw_input())
	area = math.pi * raio ** 2
	print "Área do círculo: %.2f (cm2)" % area 
