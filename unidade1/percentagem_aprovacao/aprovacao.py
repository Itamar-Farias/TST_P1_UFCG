#coding: utf-8

print "Análise da Turma"
print "==="

na = float(raw_input("Número de aprovados? "))
nr = float(raw_input("Número de reprovados? "))
nt = na + nr #Numero total de alunos
 
print "---"
print "Total de alunos na turma: %i" % nt
print "Aprovados: %i = %.1f%%" % (na, ((na/nt)*100))
print "Reprovados: %i = %.1f%%" % (nr, ((nr/nt)*100))
