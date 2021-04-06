#coding: utf-8
#UFCG - Programação I
#Itamar Farias 1152100

metros = float(raw_input())
jarda = metros/0.9144
pes = (metros * 3)/0.9144
polegadas = (metros * 36)/0.9144

print "Jardas: %.3f yd" % jarda
print "Pés: %.3f ft" % pes
print "Polegadas: %.3f in" % polegadas
