#coding: utf-8
#UFCG - Programação I
#Itamar Farias 115210021

l1 = float(raw_input()) # lado 1 do terreno
l2 = float(raw_input()) # lado 2 do terreno
area = float(raw_input()) # Área da(s) casa(s) em m²
quant_casas = ((l1*l2)/area)

print "%d casa(s) pode(m) ser construída(s) no terreno." % quant_casas
