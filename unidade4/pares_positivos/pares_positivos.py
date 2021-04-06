# coding: utf -8
# Itamar da Silva Farias
# Programação I

a = int(raw_input())
soma = 0.0
quant = 0.0
z = []
contador = 0
for n in range(a):
	b = int(raw_input())
	if b % 2 == 0:
		soma = soma + float(b)
		quant = quant + 1
		z = z + [b]

print "soma: %d" % soma
print "média: %.1f"	% (soma / quant) 	

for x in z:
	if x < (soma / quant):
		contador = contador + 1
print "%d número(s) abaixo da média" % contador
