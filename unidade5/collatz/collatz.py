# coding: utf-8
# Itamar da Silva Farias	115210021
# programação I

n = int(raw_input())
print n
while n != 1:
	if n % 2 == 0:
		n = n / 2
	else:
		n = 3 * n + 1
	print n

