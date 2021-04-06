# coding: utf-8
# Itamar da Silva Farias
# Programação I

x = int(raw_input())
y = int(raw_input())

if x <= y:
	for i in range(x, y + 1, 1):
		print "%d %d" % (i,  i**2)

elif x > y:
	print "---"
