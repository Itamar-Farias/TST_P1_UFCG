#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021


a = float(raw_input("Capacidade de revestimento? "))
print 
print "== Dados do vão a revestir =="
co = float(raw_input("Comprimento? ")) 
la = float(raw_input("Largura? "))
al = float(raw_input("Altura? "))
print
area = ((co*la)+(2*(al*co))+(2*(al*la)))
caixas = area/a
print "== Resultados =="
print "Área total a revestir: %.1f m2" % area
print "Número de caixas: %d" % caixas
