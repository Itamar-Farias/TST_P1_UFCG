# coding: utf-8
# Itamar da Silva Farias	115210021	 
# Programção I
import string
nome = raw_input()

palavra = raw_input()
numero = raw_input()
lista_numero = []
nova_palavra = []

for i in range(len(numero)-1, -1, -1):
	lista_numero.append(int(numero[i])+1)

for i in range(len(palavra)):
	nova_palavra.append(palavra[i] * lista_numero[i])

print string.join(nova_palavra, '')
