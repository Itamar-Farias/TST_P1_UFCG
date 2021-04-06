# coding: utf -8
# Itamar da Silva Farias
# Programação I

razao = int(raw_input())
quantidade = int(raw_input())
soma = 0

for n in range(quantidade):
	numero = int(raw_input())
	
for x in range(1, quantidade + 1, razao):
	soma = soma + x

print "Soma: %d." % soma
