# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

numero = raw_input()
contador = 0
contador_pares = 0
contador_impares = 0
resultado1 = ""
for i in range(0, len(numero), 2):
	contador += 1
	if int(numero[i]) % 2 == 0:
		contador_pares += 1
	else:
		contador_impares += 1
	
	
if contador_impares == contador:
	resultado1 = "verdadeiro_impar"
elif contador_pares == contador:
	resultado1 = "verdadeiro_par"

contador2 = 0
contador_pares2 = 0
contador_impares2 = 0
resultado2 = ""
	
for j in range(1, len(numero), 2):
	contador2 += 1
	if int(numero[j]) % 2 == 0:
		contador_pares2 += 1
	else:
		contador_impares2 += 1
	

if contador_impares2 == contador2:
	resultado2 = "verdadeiro_impar"
elif contador_pares == contador:
	resultado2 = "verdadeiro_par"

if resultado1 == resultado2:
	print "falso: %d algarismos." % (len(numero))
else:
	print "verdadeiro: %d algarismos." % (len(numero))
