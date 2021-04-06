# coding: utf -8
# Itamar da Silva Farias
# Programação I

racional_02 = 8.8
racional = []
for n in range(0, 456, 1):
	racional_02 = racional_02 + 0.2
	racional = racional + [racional_02]

print 8.8
for x in racional:
	print "%.1f" % x


