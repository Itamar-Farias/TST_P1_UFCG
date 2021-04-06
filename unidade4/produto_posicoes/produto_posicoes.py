# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I

numero = raw_input()
soma = 0
soma_1 = 0
novo_numero = []
for x in range(len(numero)):
	if x % 2 == 0:
		soma += int(numero[x])
		x = soma
	else:
		soma_1 += 1
		x = soma_1
	novo_numero.append(x)

print novo_numero
	
