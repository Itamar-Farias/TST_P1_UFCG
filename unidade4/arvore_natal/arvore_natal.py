#coding: utf-8
#Itamar da Silva Farias
#Programação I

altura = int(raw_input())
espaco = altura - 1
bolinha = 1

for n in range(1, altura+1, 1):
	print ((espaco * " ") + (bolinha * "o"))
	espaco = espaco - 1
	bolinha = bolinha + 2
print (((altura - 1) * " ") + "o")
