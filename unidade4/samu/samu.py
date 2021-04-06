# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

lista_mes = []
soma = 0
for x in range(12):
	atendimento =  int(raw_input())
	lista_mes.append(atendimento)
	soma += atendimento
media = float(soma) / 12
print "Média mensal de atendimentos: %.2f" % media
print "----"
for y in range(len(lista_mes)):
	if lista_mes[y] > media:
		print "Mês %d: %d" % (y + 1, lista_mes[y]) 	
