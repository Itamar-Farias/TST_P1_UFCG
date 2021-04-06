# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

n = int(raw_input())
contador = 0

while n != 1:
	contador += 1
	if n % 2 == 0:
		n = n / 2
	else:
		n = 3 * n + 1

print contador + 1
