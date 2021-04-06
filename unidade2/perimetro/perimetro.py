#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

xi = float(raw_input())
yi = float(raw_input())
xj = float(raw_input())
yj = float(raw_input())
xk = float(raw_input())
yk = float(raw_input())

didj = (((xi - xj)**2) + (((yi - yj))**2))**0.5
djdk = (((xj - xk)**2) + (((yj - yk))**2))**0.5
dkdi = (((xk - xi)**2) + (((yk - yi))**2))**0.5
perimetro = didj + djdk + dkdi

print "O perímetro é de %.2f" % perimetro
