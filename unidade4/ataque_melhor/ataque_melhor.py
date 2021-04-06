# coding: utf-8
# Itamar da Silva Farias 115210021
# Programação I

total_times = int(raw_input())
lista_times = []
lista_gols = []
total_gols = 0.0

for x in range(total_times):
	time = raw_input()
	gols = int(raw_input())
	lista_times.append(time)
	lista_gols.append(gols)
	total_gols += gols

indice = 0
time_com_mais_goals = []

for y in range(len(lista_gols)):
	if lista_gols[indice] < lista_gols[y]:
		indice = y

print "Time(s) com melhor ataque (%i gol(s)):" % lista_gols[indice]
print "%s" % lista_times[indice]
print 
print "Média de gols marcados: %.1f" % (float(total_gols) / float(total_times))

