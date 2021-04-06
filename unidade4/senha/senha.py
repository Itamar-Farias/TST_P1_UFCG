# coding: utf -8
# Itamar da Silva Farias
# Programação I

palavra = raw_input()
letra = ""

for n in palavra:		
	if n != " ":
		letra += n + n
		
	if n == " ":
		letra = n

print letra
