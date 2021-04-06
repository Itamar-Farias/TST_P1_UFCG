# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

fila_unica = raw_input().split()
n = int(raw_input())
quantidade_por_medico = len(fila_unica) / n

nova_fila = []
for i in range(len(fila_unica)):
	
