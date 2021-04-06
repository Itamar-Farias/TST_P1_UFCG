# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

nota_enem = float(raw_input())
creditos  = float(raw_input())

if nota_enem >= 600 and 0.2 * 416 < creditos < 0.9 * 416:
	print "Todas as condições satisfeitas."
elif nota_enem < 600 and creditos > 0.2 * 416 and  creditos < 0.9 * 416:
	print "Condição ENEM não satisfeita."
elif nota_enem >= 600 and creditos < 0.2 * 416:
	print "Condição CRÉDITOS não satisfeita."
elif nota_enem >= 600 and creditos > 0.9 * 416:
	print "Condição CRÉDITOS não satisfeita."
elif nota_enem < 600 and creditos < 0.2 * 416:
	print "Nenhuma condição satisfeita."
elif nota_enem < 600 and creditos > 0.9 * 416:
	print "Nenhuma condição satisfeita."
elif nota_enem >= 600 and creditos == 0.2 * 416:
	print "Todas as condições satisfeitas."
elif nota_enem >= 600 and creditos == 0.9 * 416:
	print "Todas as condições satisfeitas."
