# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

ni = int(raw_input())
print ni
while ni != 1:
	if ni % 2 == 0:
		ni = ni / 2
	else:
		ni = 3 * ni + 1
	print ni
