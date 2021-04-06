#coding: utf-8
#Itamar Farias 11210021
#Programação I

n1 = float(raw_input()) # Nota 1
n2 = float(raw_input()) # Nota 2
n3 = float(raw_input()) # Nota 3
p1 = float(raw_input()) # Peso da 1ª nota
p2 = float(raw_input()) # Peso da 2ª nota
p3 = (1-p1/100-p2/100)

print "%.1f" % n1
print "%.1f" % n2
print "%.1f" % n3
print "Média Final: %.1f" % ((n1*(p1/100))+(n2*(p2/100))+(n3*p3))
