# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def embaralhador():
	cartas = raw_input()
	monte = cartas.split()
	while True:
		operacao = raw_input()
		if operacao == "fim": break
		if operacao == "GE":
			monte.insert(0, monte[-1])
			monte.pop(-1)
		elif operacao == "GD":
			monte.append(monte[0])
			monte.pop(0)
		elif operacao == "I":
			for i in range(0, len(monte)-1, 2):
				monte[i], monte[i+1] = monte[i+1], monte[i]		
		novas_cartas = ""
		for carta in monte:
			if novas_cartas == "":
				novas_cartas += carta
			else:
				novas_cartas += " " + carta
		print novas_cartas
	
embaralhador()
