# coding: utf -8
# Itamar da Silva Farias
# Programação I

l = []
for n in range(0, 2, 1):
	num_1, num_2 = raw_input().split()
	num_1, num_2 = float(num_1), float(num_2)
	calc = (num_1 - num_2) 
	l = l + [calc]
	
for x in l:
	if x >= 0:
		print " %3.1f" % x
	elif x < 0:
		print " %4.1f" % x

