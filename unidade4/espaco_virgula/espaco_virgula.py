# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

frase = raw_input()
i = int(raw_input())
j = int(raw_input())
nova_frase = ""

for x in range(i,j):
	if frase[x] == ' ':
		nova_frase += ', '
	elif x == j-1:
		nova_frase += frase[x]
	elif x != j:
		nova_frase += frase[x] + ' '
print nova_frase
