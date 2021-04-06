# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

registro = []
soma = 0

while True:
	soma = 0
	codigo = raw_input().split()
	if codigo[0] == "S":
		break
	if codigo[0] == "R":
		for x in codigo[1]:
			if x not in ("0,1,2,3,4,5,6,7,8,9,"):
				registro.append(x)
	elif codigo[0] == "P":
		for y in registro:
			if codigo[1] == y:
				soma += 1
		print soma
