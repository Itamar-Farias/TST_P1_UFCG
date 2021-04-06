# coding: utf-8
# Itamar da SIlva Farias	115210021
# Programação I

import math

lado = float(raw_input())
raio = lado / 2 ** 0.5

perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print "Perímetro: %.5f" % perimetro
print "Área: %.5f" % area
