

import math

print "Cálculo da Superfície de um Cilindro"
print "---"

diametro = float(raw_input("Medida do diâmetro? "))
altura = float(raw_input("Medida da altura? "))
area = 2 * math.pi * (diametro/2) * (altura + diametro / 2) 

print "---"
print "Área calculada: %.2f" % area
