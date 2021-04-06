# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I

def pivot(numeros):
	pivor = 0
	for i in range(1, len(numeros), 1):
		if int(numeros[i]) <= int(numeros[pivor]):
			for j in range(i, pivor, -1):
				numeros[j], numeros[j - 1] = numeros[j - 1],  numeros[j]
			if numeros[pivor] < numeros[pivor + 1]:
				pivor += 1
