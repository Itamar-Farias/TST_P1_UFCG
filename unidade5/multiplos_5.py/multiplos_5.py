# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

while True:
	numero = int(raw_input())
	for x in range(1, numero):
		if x % 2 == 0 and x % 5 == 0:
			print x
	break 
