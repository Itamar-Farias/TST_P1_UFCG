# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

simbols = {"H": 1, "S": 32, "O": 16, "C": 12, "Ca": 40, "Na": 23, "P": 31}

def soma_elementos(elemento):
	soma = 0
	for i in range(len(elemento)-1):
		if elemento[i+1].isdigit():
			soma += simbols[elemento[i]] * int(elemento[i+1])
		else:
			if elemento[i].isdigit() == False:
				soma += simbols[elemento[i]]
	if elemento[-1].isdigit() == False:
		soma += simbols[elemento[-1]]
	return soma
	
while True:
	dado = raw_input().split()
	if dado[0] == "fim": break
	print soma_elementos(dado)
