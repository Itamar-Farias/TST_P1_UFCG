# coding: utf -8
# Itamar da Silva Farias
# Programação I

valores_meses = []
meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
indice = 0 

for n in range(12):
	a, b = raw_input().split()
	a, b = float(a), float(b)
	lucro = a - b
	valores_meses = valores_meses + [lucro]
	
for x in valores_meses:
	if x >= 0:
		print "%s  %.1f" % (meses[indice], x)
	if x < 0:
		print "%s %.1f" % (meses[indice], x)
	indice = indice + 1
