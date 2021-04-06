# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

soma = 0
lista_numero = []
while True:
	numero = raw_input()
	if numero == "fim":
		break
	soma += float(numero)
	lista_numero.append(float(numero))

media = soma / len(lista_numero)

for x in range(len(lista_numero)):
	if lista_numero[x] > media:
		print "%d, %.2f > %.2f" % (x, lista_numero[x], media)
		break
