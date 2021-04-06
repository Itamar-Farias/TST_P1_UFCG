# coding: utf-8
# Itamar da Silva Farias 115210021
# Programação I

posicao_inicial = float(raw_input("Posição inicial? "))
velocidade_inicial = float(raw_input("Velocidade inicial? "))
tempo = float(raw_input("Tempo? "))
aceleracao = float(raw_input("Aceleração? "))

posicao_final = posicao_inicial + (velocidade_inicial * tempo) + (aceleracao * tempo ** 2 / 2)
distancia = posicao_final - posicao_inicial
velocidade_media = distancia / tempo
velocidade_final = velocidade_inicial + aceleracao * tempo

print ""
print "Dados da questão"
print "================"
print "   Posição inicial: %.2f m" % posicao_inicial
print "Velocidade inicial: %.2f m/s" % velocidade_inicial
print "        Aceleração: %.2f m/s2" % aceleracao
print "             Tempo: %.2f s" % tempo
print "  Velocidade final: %.2f m/s" % velocidade_final
print "  Velocidade média: %.2f m/s" % velocidade_media
print "     Posição final: %.2f m" % posicao_final
