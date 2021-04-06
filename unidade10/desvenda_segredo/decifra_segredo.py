# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def decifra(chave,mensagem):
	decifrado = ""
	for i in range(len(mensagem)):
		if mensagem[i] in chave:
			decifrado += chave[mensagem[i]]
		else:
			decifrado += mensagem[i]
	

	return decifrado
