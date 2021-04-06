# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

palavra = raw_input()
senha =  ""
troca = 0
for x in range(1, len(palavra)):
	if palavra[x] == "a" or palavra[x] == "A":
		senha += "4"
		troca += 1
	elif palavra[x] == "e" or palavra[x] == "E":
		senha += "3"
		troca += 1
	elif palavra[x] == "i" or palavra[x] == "I":
		senha += "1"
		troca += 1
	elif palavra[x] == "o" or palavra[x] == "O":
		senha += "0"
		troca += 1
	else:
		senha += palavra[x]

print "%s (%d troca(s))" % ((palavra[0] + senha), troca)
