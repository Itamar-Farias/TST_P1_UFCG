# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

quantidade_notas =  int(raw_input())
soma = 0
final = 0
soma_final = 0
total = 0.0

for x in range(quantidade_notas):
	nota = float(raw_input())
	if nota >= 4.0 and nota < 7.0:
		final += 1
		soma_final += nota
	total += nota

percentual = (float(final) / quantidade_notas) * 100.0

print "%d (%.1f%%) alunos na final" % (final, percentual)
if soma_final != 0:
	media = soma_final / final 
	print "Média das notas: %.1f" % media
