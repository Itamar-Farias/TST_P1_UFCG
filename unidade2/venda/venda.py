#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

a = float(raw_input()) # Custo de entrada
b = float(raw_input()) # Percentual de despesas indiretas
c = float(raw_input()) # Percentual do lucro desejado
d = float(raw_input()) # Percentual de impostos
e = float(raw_input()) # Percentual de comissões
f = float(raw_input()) # Percentual de descontos
g = float(raw_input()) # Percentual de encargos

preco = a+((b/100+c/100+d/100-e/100-f/100-g/100)*a)

print preco


"""preco = ((a+b+c)*100)/(100-(d/100)-(e/100)-(f/100)-(g/100))"""
"""preco = (((b/100+c/100)*a)+a)-(((d/100+e/100+f/100+g/100)*a)+a) 
"""
