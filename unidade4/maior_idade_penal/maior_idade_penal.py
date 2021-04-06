# coding: utf-8
# Itamar da Silva Farias	1152210021	
# Programação I

nomes = raw_input().split()
idade = raw_input().split()
lista_nomes = [nomes]
lista_idades = [idade]
soma = 0

for x in lista_idades:
	if x >= 18:
		soma += 1

print soma
		
