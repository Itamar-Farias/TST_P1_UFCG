# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def excesso_127(numero):
	numero = bin(numero + 127)
	numero = str(numero[2:])
	if len(numero) < 8:
		multi = 8 - len(numero)
		numero = (multi * "0") + numero
	return numero

def complemento1(numero):
	sinal = numero
	if numero < 0:
		numero = bin(numero)[3:]
	else:
		numero = bin(numero)[2:]
	if sinal < 0:
		if len(numero) < 8:
			multi = 8 - len(numero)
			numero = (multi * "0") + numero
		novo_numero = ""
		for i in numero:
			if i == "0":
				novo_numero += "1"
			elif i == "1":
				novo_numero += "0"
		numero = novo_numero
	else:
		if len(numero) < 8:
			multi = 8 - len(numero)
			numero = (multi * "0") + numero			
	return numero

while True:
	dados = raw_input().split()
	if dados[0] == "***": break
	if dados[0][0] == "C":
		print complemento1(int(dados[1]))
	else:
		print excesso_127(int(dados[1]))
