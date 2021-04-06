# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

delta = (b ** 2) - (4 * a * c)

if delta < 0:
	print "sem raizes reais"

else:
	x1 = (-b + delta ** 0.5) / (2 * a)
	x2 = (-b - delta ** 0.5) / (2 * a)
	if x1 == x2:
		print "x = %.2f" % x1
	else:
		print "x1 = %.2f" % x1
		print "x2 = %.2f" % x2
