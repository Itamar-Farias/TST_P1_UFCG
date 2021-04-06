# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', \
		 'jul', 'ago', 'set', 'out', 'nov', 'dez']

saldo  = 0
maior  = 0
indice = 0

for i in range(12):
	saldo += 500
	mes = int(raw_input())
	saldo -= mes
	if saldo >= maior:
		maior = saldo
		indice = i

print meses[indice] 
