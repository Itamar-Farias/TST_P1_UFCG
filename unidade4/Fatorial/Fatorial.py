# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

numero = int(raw_input())
fatorial = 1
for x in range(numero, 0, -1):
	fatorial = fatorial * x 

print fatorial
