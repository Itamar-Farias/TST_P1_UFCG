# coding: utf-8
# Itamar da Silva Farias 115210021	
# Programação I

bolinhas = 1
espacos = 4

for n in range(1, 6, 1):
	print ((espacos * " ") + bolinhas * "o")
	bolinhas = bolinhas + 2
	espacos = espacos - 1
print "    o"
