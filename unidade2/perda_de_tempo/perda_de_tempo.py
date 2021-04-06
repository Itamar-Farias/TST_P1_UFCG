#coding:utf-8
#Itamar da Silva Farias 115210021	
#Programação I

segunda = float(raw_input())
terca = float(raw_input())
quarta = float(raw_input())
quinta = float(raw_input())
sexta = float(raw_input())

total = segunda + terca + quarta + quinta + sexta
media = (segunda + terca + quarta + quinta + sexta) / 5.0
episodio = total / 50
percentual = (total * 100) / 7200

print "Você perdeu %d min na semana (média de %.1f min por dia)." % (total, media)
print "Isso significa %.2f%% da sua semana produtiva." % percentual
print "Daria para assistir %d episódio(s) de House." % episodio
