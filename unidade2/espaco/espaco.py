#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

nome1 = raw_input() #Usuário 1
e = float(raw_input()) # espaço em disco (em bytes)-1
nome2 = raw_input() #Usuário 2
f = float(raw_input()) # espaço em disco (em bytes)-2
nome3 = raw_input() #Usuário 1
g = float(raw_input()) # espaço em disco (em bytes)-3

print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado"
print 

espaco1 = ((e/1024)/1024)
espaco2 = ((f/1024)/1024)
espaco3 = ((g/1024)/1024)

print "1, %s, %.2f MB" % (nome1, espaco1)
print "2, %s, %.2f MB" % (nome2, espaco2)
print "3, %s, %.2f MB" % (nome3, espaco3)
print 
print "Espaço total ocupado: %.2f MB" % (espaco1 + espaco2 + espaco3)
print "Espaço médio ocupado: %.2f MB" % ((espaco1 + espaco2 + espaco3)/3)
