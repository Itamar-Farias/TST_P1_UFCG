# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

def func():
	while True:
		nova_palavra = ""
		palavra = raw_input().split()
		if palavra[0] == "fim":
			break
		for i in range(len(palavra)):
			if i > 0:
				nova_palavra += len(palavra[i - 1]) * "*"
			for j in range(len(palavra[i])):
				if palavra[i][j] == palavra[i][j].lower():
					nova_palavra += palavra[i][j].upper()
				elif palavra[i][j] == palavra[i][j].upper():
					nova_palavra += palavra[i][j].lower()
				elif palavra[i][j] == " ":
					nova_palavra += len(palavra)[i] * "*"
	
		nova_palavra2 = ""	
		for k in range(len(nova_palavra)):
			if nova_palavra[k] in "A, a":
				nova_palavra2 += "4"
			elif nova_palavra[k] == "4":
				nova_palavra2 += "A"
			elif nova_palavra[k] in "B, b":
				nova_palavra2 += "8"
			elif nova_palavra[k] == "8":
				nova_palavra2 += "B" 
			elif nova_palavra[k] in "E, e":
				nova_palavra2 += "3"
			elif nova_palavra[k] == "3":
				nova_palavra2 += "E"
			elif nova_palavra[k] in "G, g":
				nova_palavra2 += "6"
			elif nova_palavra[k] == "6":
				nova_palavra2 += "G"
			elif nova_palavra[k] in "I, i":
				nova_palavra2 += "1"
			elif nova_palavra[k] == "1":
				nova_palavra2 += "I" 
			elif nova_palavra[k] in "L, l":
				nova_palavra2 += "7"
			elif nova_palavra[k] == "7":
				nova_palavra2 += "L"
			elif nova_palavra[k] in "S, s":
				nova_palavra2 += "5"
			elif nova_palavra[k] == "5":
				nova_palavra2 += "S" 
			elif nova_palavra[k] in "O, o":
				nova_palavra2 += "0"
			elif nova_palavra[k] == "0":
				nova_palavra2 += "O"
			else:
				nova_palavra2 += nova_palavra[k]
			
			
		print nova_palavra2
func()
