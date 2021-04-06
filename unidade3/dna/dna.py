# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

dna1 = raw_input()
dna2 = raw_input()
dna3 = raw_input()

menor_dna = dna1

if len(dna2) < len(menor_dna):
	menor_dna = dna2
	if len(dna3) < len(menor_dna):
		menor_dna = dna3

elif len(dna3) < len(menor_dna):
	menor_dna = dna3
	
print menor_dna, len(menor_dna)

