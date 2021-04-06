# coding: utf -8
# Itamar da Silva Farias
# Programação I

controle = int(raw_input())
total_times = []
total_goals = []
total = 0.0

for n in range(controle):
	time = raw_input()
	goals = int(raw_input())
	total_times = total_times + [time]
	total_goals = total_goals + [goals]







for x in total_goals:
	total = total + x

print "Média de gols marcados: %.1f" % (float(total) / controle)
