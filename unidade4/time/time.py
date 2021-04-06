# coding: utf-8

quantidade_times = int(raw_input())
lista_times = []
lista_goals = []
indice = 0
total_goals = 0

for n in range(quantidade_times):
	time = raw_input()
	goals = int(raw_input())
	lista_times.append(time)
	lista_goals.append(goals)

for x in range(1, len(lista_goals)):
	if lista_goals[indice] < lista_goals[x]:
		indice = x

print "Time(s) com melhor ataque (%d gol(s)):" % lista_goals[indice]
print "%s" % lista_times[indice]
print
for y in lista_goals:
	total_goals += y

media = (float(total_goals)) / (float(quantidade_times))

print "Média de gols marcados: %.1f"  % media
