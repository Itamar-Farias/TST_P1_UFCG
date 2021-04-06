# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I

palavra = raw_input()

nova_palavra = ""

for x in range(len(palavra)):
	if palavra[x] != " ":
		nova_palavra += palavra[x]


nova_palavra_1 = ""
for y in range(len(palavra[::-1])):
	if palavra[::-1][y] != " ":
		nova_palavra_1 += palavra[::-1][y]

if nova_palavra == nova_palavra_1:
	print "%s é palíndromo" % palavra
else:
	print "%s não é palíndromo" % palavra
