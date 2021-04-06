#coding: utf-8
print "== Estágio 1 =="
p1 = float(raw_input("Peso? "))
n1 = float(raw_input("Nota? "))
print "== Estágio 2 =="
p2 = float(raw_input("Peso? "))
n2 = float(raw_input("Nota? "))
print "== Estágio 3 =="
p3 = float(raw_input("Peso? "))
n3 = float(raw_input("Nota? "))
media = (p1*n1+p2*n2+p3*n3)
print "== Resultados =="
print "Média parcial: %.1f" % media
print "Nota na final, pra média 5.0 = %.1f" % (((5.0-(media*0.6))/0.4))
print "Nota na final, pra média 7.0 = %.1f" % (((7.0-(media*0.6))/0.4))
