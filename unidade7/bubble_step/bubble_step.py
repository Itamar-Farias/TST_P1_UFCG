# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def bubble_step():
	sequencias = []
	while True:
		sequencia = raw_input().split()
		if sequencia[0] == "fim":
			break
		sequencias.append(sequencia)

	for i in sequencias:
		for k in range(len(i) - 1):
			if int(i[k]) > int(i[k + 1]):
				i[k], i[k + 1] = i[k+1], i[k]
		print " ".join(i)
				
bubble_step()
