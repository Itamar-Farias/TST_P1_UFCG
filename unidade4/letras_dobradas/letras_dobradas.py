# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

quantidade = int(raw_input())
com_letras = 0
sem_letras = 0
lista_com = []
lista_sem = []

for i in range(quantidade):
	achou = 'nao'
	palavra = raw_input()
	for i in range(len(palavra)-1):	
		if palavra[i] == palavra[i+1]:
			achou = 'sim'
			com_letras += 1
			lista_com.append(palavra)
			break
	if achou == 'nao':
		sem_letras += 1
		lista_sem.append(palavra)
		
print '%d palavra(s) com letras dobradas:' % com_letras
for palavra in lista_com:
	print palavra
print '---'
print '%d palavra(s) sem letras dobradas:' % sem_letras
for palavra in lista_sem:
	print palavra
