#coding: utf-8
n1 = float(raw_input()) # Nota 1
n2 = float(raw_input()) # Nota 2
n3 = float(raw_input()) # Nota 3
p1 = float(raw_input()) # Peso da 1ª nota
p2 = float(raw_input()) # Peso da 2ª nota

print "Média Final: %.1f" % ((n1*(p1/100))+(n2*(p2/100))+(n3*(1-p1/100-p2/100)))
